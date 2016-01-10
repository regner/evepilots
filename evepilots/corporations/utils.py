

from evepilots.extensions import db
from evepilots.corporations.models import CorporationModel


def ensure_corp_exists(corporation_id):
    """ Ensures a given corporation ID exists or creates it in the DB.

    :param corporation_id: The corporation ID to confirm exists in the DB.
    """

    corporation = CorporationModel.query.get(corporation_id)

    if corporation is not None:
        return

    corporation = CorporationModel()
    corporation.id = corporation_id

    db.session.add(corporation)
    db.session.commit()
