import requests
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
        return "Error: auth wrong params", 401

    application = AppRepository().get_app_by_bundle(bundle)

    if not application:
        return 'Error: app is not exist', 402

    if check_available_page(application['url']):
        return 'Error: page is available', 403

    if not AppRepository().ban_app_by_bundle(bundle):
        return 'Error: app is already banned', 404

    NotificationUsers().ban_application_notify(application)

    print(f"successfully banned: {application['bundle']}")
    return 'App was banned successfully', 201


def check_available_page(url) -> bool:
    return requests.head(url).status_code == 200


if __name__ == '__main__':
    # app.run()
    http_server = WSGIServer(("0.0.0.0", 5020), app)
    http_server.serve_forever()
