import os
from dotenv import load_dotenv
from pathlib import Path


class Config:
    @staticmethod
    def get_config():
        path = os.getcwd()
        path = '/Users/andycarter/develop/pycharm/flask_projects/thepubpicker'
        # print('path', path)
        total_path = path + '/.env'

        dotenv_path = Path(total_path)
        load_dotenv(dotenv_path=dotenv_path)

        config = {
            "ACCESS_ID": os.environ.get("ACCESS_ID"),
            "ACCESS_KEY": os.environ.get("ACCESS_KEY"),
            "CONTACT_TEL": os.environ.get("CONTACT_TEL")}
        return config
