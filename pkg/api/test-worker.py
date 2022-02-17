from pkg.api import util
from flask import Flask, jsonify
from flask.views import MethodView
import pkg.kubeapi
import pkg.log
import logging

logger = logging.getLogger()
util.logger = logger
kubeapi = pkg.kubeapi.__kubeapi()
setting = pkg.log.load_setting("./setting.txt")


class test_worker(MethodView):
    def get(self, method):
        if (not method in ["GET"]):
            return jsonify({"status":"unsuccess"})
        try:
            all_worker = kubeapi.get_all_worker(setting["WORKER_NAME"])
            for worker_name, spec in all_worker.items():
                logger.info(worker_name, util.__call_api(f"http:{spec.pod_ip}:8080/test/GET"))

            return jsonify({"status":"success", "data":all_worker})
        except Exception as e:
            return jsonify({"status":"success"})
        

def add_url_rule(app):
    _api = test_worker.as_view(f'test_worker')
    app.add_url_rule(f'/test-worker/<method>', view_func=_api, methods=["GET"])


def set_logger(pass_logger):
    logger = pass_logger
    util.logger = logger
