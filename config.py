import os

from dotenv import load_dotenv

load_dotenv()


class RatingsConfig:
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @classmethod
    @property
    def SQLALCHEMY_DATABASE_URI(self):
        return os.environ.get('SQLALCHEMY_DATABASE_URI', '')