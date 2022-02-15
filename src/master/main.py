import flask
from pkg import log

#load setting and get logger
setting = log.load_setting("./setting/setting.txt")
logger = log.get_logger(setting=setting)


def main():
    #load api
    from pkg.api import api as api

    from flask import Flask
    from flask_cors import CORS
    app = Flask(__name__)
    cors = CORS(app)
    app.config['CORS_HEADERS'] = "Content-Type"
    app.config['JSON_AS_ASCII'] = False


if (__name__ == "__main__"):
    main()
