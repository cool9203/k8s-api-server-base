from pkg import log
from flask import Flask
from flask_cors import CORS
import ast
import importlib
from waitress import serve

#load setting and get logger
setting = log.load_setting("./setting/setting.txt")
logger = log.get_logger(setting=setting, name="master")


def main():
    app = Flask(__name__)
    cors = CORS(app)
    app.config['CORS_HEADERS'] = "Content-Type"
    app.config['JSON_AS_ASCII'] = False

    ip = setting.get("IP", "0.0.0.0")
    port = int(setting.get("PORT", 8080))
    develope = setting.get("DEVELOPE", "false")
    debug = setting.get("DEBUG", "true")

    logger.info(f"ip:{ip}")
    logger.info(f"port:{port}")
    logger.info(f"develope:{develope}")
    logger.info(f"debug:{debug}")

    #dynamic load api
    api_name_list = ast.literal(setting.get("MASTER_API", "[]"))

    api_list = list()
    for api_name in api_name_list:
        try:
            api = importlib.import_module(f"pkg.api.{api_name}")
            api_list.append(api)
            logger.info(f"load {api_name} finish.")
        except Exception as e:
            logger.warning(e)

    for api in api_list:
        api.add_url_rule(app)

    #open flask server
    if (develope.lower() == "true"):
        if (debug.lower() == "false"):
            app.run(host=ip, port=port, debug=False)
        else:
            app.run(host=ip, port=port, debug=True)
    elif (develope.lower() == "false"):
        from waitress import serve
        serve(app, host=ip, port=port)
    else:
        logging.critical("api server not create.")


if (__name__ == "__main__"):
    main()
