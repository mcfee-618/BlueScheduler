from flask import Flask
from BlueScheduler.conf.logger_conf import LoggerConfig
from BlueScheduler.log.logger import init_log
import BlueScheduler.routes as route


def create_app():
    app = Flask("blue_scheduler")
    register_routes(app)
    register_logger()
    return app

def register_routes(app):
    app.register_blueprint(route.admin_bp, url_prefix='/admin')
    app.add_url_rule(rule="/", endpoint="index", view_func=route.index)
    
def register_logger():
    logger_conf = LoggerConfig.get_logger_conf("server")
    init_log(logger_conf)
    