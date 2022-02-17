import logging
logger = logging.getLogger()

from flask import request
import json

def get_request_data():
    #get data, and all data key change to capital letter
    json_data = request.data.decode("utf-8").replace("\'", "\"")
    form_data = request.form.to_dict(flat=False)
    logger.debug(f"get json_data : {json_data}")
    logger.debug(f"get form_data : {form_data}")
    data = dict()
    try:
        data = json.loads(json_data)
    except:
        pass

    data.update(form_data)

    logger.debug(f"get data : {data}")
    data = {k.upper():v for k, v in data.items()}
    return data
