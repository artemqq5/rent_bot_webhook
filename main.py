from gevent.pywsgi import WSGIServer

from flask import Flask, request

from config import WEBHOOK_PASSWORD
from data.repository.AppRepository import AppRepository
from domain.notify.NotificationUsers import NotificationUsers

app = Flask(__name__)


@app.route("/flows", methods=['GET'])
def web_handler():
    bundle = request.args.get("bundle", None)
    key = request.args.get("key", None)

    if not bundle or not key or key != WEBHOOK_PASSWORD:
        return "Error auth", 201

    application = AppRepository().get_app_by_bundle(bundle)

    if not application:
        return 'Error app', 202

    if not AppRepository().ban_app_by_bundle(bundle):
        return 'Error bun', 203

    NotificationUsers().ban_application_notify(application)

    return 'OK', 200


if __name__ == '__main__':
    # app.run()
    http_server = WSGIServer(("0.0.0.0", 5020), app)
    http_server.serve_forever()
