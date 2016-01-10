

from evepilots.extensions import db


class CorporationModel(db.Model):
    """
        Model for individual Corporations.
    """

    __tablename__ = 'corporations'

    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    name = db.Column(db.String(length=256))
    last_checked = db.Column(db.DateTime)
    capsuleers = db.relationship('CapsuleerModel', backref='corporation', lazy='dynamic')
