

from datetime import datetime

from evepilots.extensions import db


class CapsuleerModel(db.Model):
    """
        Model for individual Capsuleers.
    """

    __tablename__ = 'capsuleers'

    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    name = db.Column(db.String(length=256))
    corporation_id = db.Column(db.Integer, db.ForeignKey('corporations.id'))
    security_status = db.Column(db.Integer)
    last_checked = db.Column(db.DateTime)
    corp_history = db.relationship('CapsuleerCorpHistory', lazy='dynamic')
    sec_status_history = db.relationship('CapsuleerSecStatusHistory', lazy='dynamic')


class CapsuleerCorpHistory(db.Model):
    """
        Model for tracking a capsuleers corp history.
    """

    __tablename__ = 'capsuleers_corporation_history'

    id = db.Column(db.Integer, primary_key=True)
    capsuleer_id = db.Column(db.Integer, db.ForeignKey('capsuleers.id'))
    corporation_id = db.Column(db.Integer, db.ForeignKey('corporations.id'))
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)


class CapsuleerSecStatusHistory(db.Model):
    """
        Model for tracking a capsuleers security status changes over time.
    """
    
    __tablename__ = 'capsuleers_secstatus_history'
    
    id = db.Column(db.Integer, db.ForeignKey('capsuleers.id'), primary_key=True)
    sec_status = db.Column(db.Float)
    datetime = db.Column(db.DateTime, default=datetime.utcnow)
