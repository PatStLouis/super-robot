from os import environ, path
from dotenv import load_dotenv
import json

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))

class Config(object):
    ENV = "development"
    DEBUG = True
    SECRET_KEY = "my_secret_key"

    GUAC_PASSWORD = "UtQ8XYdaY59gzN3K9aVmMzdAnzUkV8MY"

    with open("app/static/data/users.json", "r") as f:
            users = json.loads(f.read())

    USERS = users
