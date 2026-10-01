import os


SECRET_KEY = os.environ["SECRET_KEY"]
API_URL = os.environ["API_URL"]


class Config:
    SECRET_KEY = SECRET_KEY
    API_URL = API_URL
