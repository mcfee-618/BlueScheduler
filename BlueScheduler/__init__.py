from flask import Flask, Request, Response
import BlueScheduler.routes as route


def create_app():
    app = Flask("blue_scheduler")
    register_routes(app)
    return app

def register_routes(app):
    app.register_blueprint(route.admin_bp, url_prefix='/admin')
    app.add_url_rule(rule="/", endpoint="index", view_func=route.index)
