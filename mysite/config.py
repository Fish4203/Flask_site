import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'wefbibgh32uh23u88u8o99p33huu3e8299e984747y3g2ifei9'

    SQLALCHEMY_DATABASE_URI = os.environ.get('Database_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')

    SQLALCHEMY_TRACK_MODIFICATIONS = False
