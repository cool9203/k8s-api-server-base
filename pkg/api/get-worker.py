from pkg.api import util
from flask import Flask, jsonify
from flask.views import MethodView
import pkg.kubeapi
import pkg.log
import pkg.dbapi
import logging
import yaml
from pathlib import Path

logger = logging.getLogger(__name__)
kubeapi = pkg.kubeapi.__kubeapi()

worker_name = pkg.dbapi.get_worker_name()

class get_worker(MethodView):
    def get(self, method):
        if (not method in ["GET"]):
            return jsonify({"status":"unsuccess"})
        try:
            return jsonify({"status":"success", "data":kubeapi.get_all_worker(worker_name)})
        except Exception as e:
            return jsonify({"status":"success"})
        

def add_url_rule(app):
    _api = get_worker.as_view(f'get_worker')
    app.add_url_rule(f'/worker/<method>', view_func=_api, methods=["GET"])
