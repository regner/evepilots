

import logging

from datetime import datetime

from sqlalchemy.sql.expression import nullsfirst

from flask.ext.servicelayer import SQLAlchemyService

from evepilots.extensions import db, celery, evelink_eve
from evepilots.capsuleers.models import CapsuleerModel, CapsuleerCorpHistory, CapsuleerSecStatusHistory
from evepilots.utils.evelink import evelink_ts_to_datetime
from evepilots.corporations.utils import ensure_corp_exists


log = logging.getLogger('evepilots.capsuleers.services')


class CapsuleerService(SQLAlchemyService):
    __model__ = CapsuleerModel
    __db__ = db
    
    def get_needing_update(self, quantity=10):
        """
            Gets a number of capsuleers ordered by their last_checked value with
            nulls coming first.
            
            :param quantity: the number of capsuleers to be returned
        """
        
        log.info('Finding {} capsuleers to update.'.format(quantity))
        
        order_by = nullsfirst(self.__model__.last_checked.asc())
        
        return self._find().order_by(order_by).limit(quantity)
    
    @celery.task
    def update_information(self, model):
        """
            Updates a given capsuleer model and triggers an update of the
            corasponding CapsuleerCorpHistory model.
            
            :param model: the model of a capsuleer to be updated
        """
        
        log.info('Updating the information for capsuleer {}'.format(model.id))
        
        self._isinstance(model)
        
        capsuleer_info = evelink_eve.character_info_from_id(model.id).result
        capsuleer_corp_history.update_from_id(model.id)
        capsuleer_sec_history.create(**{
            'id': model.id,
            'sec_status': capsuleer_info['sec_status'],
        })
    
        ensure_corp_exists(capsuleer_info['corp']['id'])
        
        # TODO: Potential DB performance increase in only updating columns that
        # have changed.
        self.update(model, **{
            'name': capsuleer_info['name'],
            'security_status': capsuleer_info['sec_status'],
            'last_checked': datetime.now(),
            'corporation_id': capsuleer_info['corp']['id'],
        })
    
    def get_newest_updates(self, quantity=7):
        """
            Returns a sorted list of the most recently updated capsuleers.
            
            :param quantity: the number of capsuleers to return
        """
        
        log.info('Fetching {} of the most recently updated capsuleers.'.format(quantity))
        
        filters = self.__model__.last_checked != None
        order_by = self.__model__.last_checked.desc()
        
        return self.__model__.query.filter(filters).order_by(order_by).limit(quantity)
        
    def count(self):
        """
            Returns the total number of rows in for this model.
        """
        
        return self.__model__.query.count()


class CapsuleerCopHistoryService(SQLAlchemyService):
    __model__ = CapsuleerCorpHistory
    __db__ = db

    def get_capsuleer_history(self, id):
        """
            Gets all of the history for a given capsuleer ID and ordered by
            their start_time descending.
            
            :param id: id for the capsuleer to lookup
        """
        
        return self._find(capsuleer_id=id).order_by(self.__model__.start_time.desc())
        

    def update_from_id(self, id):
        """
            Given a capsuler ID updates the capsuleers corporation history.
            
            :param id: id of the capsuleer to update
        """
        
        api_history = evelink_eve.character_info_from_id(id).result['history']
        db_history = self.get_capsuleer_history(id).all()
        
        if len(api_history) != len(db_history):
            api_history = list(reversed(api_history))
            db_history = list(reversed(db_history))
            
            for index, corp in enumerate(api_history[len(db_history) - 1:]):
                ensure_corp_exists(corp['corp_id'])
                
                model_data = {
                    'capsuleer_id': id,
                    'corporation_id': corp['corp_id'],
                    'start_time': evelink_ts_to_datetime(corp['start_ts']),
                }
                
                # TODO: Add logic for adding end_time
                
                self.create(**model_data)
    
    def get_birthday_from_id(self, id):
        """
            Gets a the birthday for a given capsuleer id.
        """
        
        return self._find(capsuleer_id=id).order_by(self.__model__.start_time.asc()).first()


class CapsuleerSecStatusService(SQLAlchemyService):
    __model__ = CapsuleerSecStatusHistory
    __db__ = db


capsuleers = CapsuleerService()
capsuleer_corp_history = CapsuleerCopHistoryService()
capsuleer_sec_history = CapsuleerSecStatusService()