

import os


class AppConfig(object):
    DEBUG = True
    SECRET_KEY = os.environ.get('EPI_SECRET_KEY', 'ThisIsJustTheDevKey')
    SQLALCHEMY_DATABASE_URI = os.environ.get('EPI_SQLA_URI', 'postgresql://postgres:epi@192.168.99.100:32769/')
    CELERY_BROKER_URL = os.environ.get('EPI_CELERY_BROKER_URL', 'redis://192.168.99.100:32768/0')
