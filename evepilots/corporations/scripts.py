

from datetime import datetime

from evelink.eve import EVE
from flask.ext.script import Command

from evepilots.corporations.models import CorporationModel
from evepilots.extensions import db


class UpdateExistingCorporations(Command):
    """ Selects a number of existing corporations and updates them. """

    def run(self):
        pass
