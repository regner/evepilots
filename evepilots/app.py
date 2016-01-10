

from flask import Flask

from evepilots.config import AppConfig
from evepilots.extensions import configure_extensions
from evepilots.utils.processors import configure_processors
from evepilots.utils.blueprints import configure_blueprints


def create_app():
    """
        Creates the app object.
    """

    app = Flask(__name__)
    app.config.from_object(AppConfig)

    configure_blueprints(app)
    configure_extensions(app)
    configure_processors(app)

    return app
