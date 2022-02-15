import yaml
import logging
import logging.config
from pathlib import Path


def load_setting(log_path=""):
    setting = dict()
    if (not Path(log_path).exists()):
        raise Exception(f"'{log_path}' setting not exists")
    with Path(log_path).open("r", encoding="utf8") as f:
        for line in f.readlines():
            line = line.replace("\n", "").replace("\t", "").replace("\r", "").replace(" ", "")
            if (line[0] == "#"):
                continue
            else:
                line_split = line.split("#")
                key = line_split[0].split("=")[0].upper()
                value = line_split[0].split("=")[1]
                setting[key] = value
    return setting


def get_logger(**kwargs):
    params = locals()["kwargs"]
    name = params.get("name", "root")
    try:
        log_path = params["logging_config_path"] if "logging_config_path" in params else params.get("setting")["LOGGING_CONFIG_PATH"]
        with Path(log_path).open("r", encoding="utf8") as f:
            logging.config.dictConfig(yaml.load(f, Loader=yaml.FullLoader))
    except Exception as e:
        print("not load logging-config")
        print(f"get_logger : {e}")
    return logging.getLogger(name)
