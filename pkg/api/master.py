import importlib
import logging
logger = logging.getLogger(f"master.{__name__}")

using_api_name_list = ["test", "get-worker", "test-worker"]


api_list = list()
for api_name in using_api_name_list:
    try:
        api = importlib.import_module(f"pkg.api.{api_name}")
        api_list.append(api)
    except Exception as e:
        logger.error(e)


def add_url_rule(app):
    for api in api_list:
        api.add_url_rule(app)
        api.set_logger(logger)
        logger.info(f"load api : {api.__name__}")
