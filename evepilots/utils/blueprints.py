

from evepilots.public.views import blueprint as public_blueprint
from evepilots.capsuleers.views import blueprint as capsuleers_blueprint


def configure_blueprints(app):
    """
        Registers all relevant blueprints with the app.
    """

    app.register_blueprint(public_blueprint)
    app.register_blueprint(capsuleers_blueprint)