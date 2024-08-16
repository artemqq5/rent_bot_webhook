import threading
import time

import requests
from flask import Flask, request
from gevent.pywsgi import WSGIServer

from config import WEBHOOK_PASSWORD
from data.repository.AppRepository import AppRepository
from domain.notify.NotificationUsers import NotificationUsers

app = Flask(__name__)


@app.route("/flows", methods=['GET'])
def web_handler():
    bundle = request.args.get("bundle", None)
    key = request.args.get("key", None)
    print(bundle)

    if not bundle or not key or key != WEBHOOK_PASSWORD:
        print('Error: auth wrong params')
        return "Error: auth wrong params", 401

    application = AppRepository().get_app_by_bundle(bundle)

    if not application:
        print('Error: app is not exist')
        return 'Error: app is not exist', 402

    # Запуск фонової задачі
    threading.Thread(target=delayed_check, args=(application,)).start()

    return 'OK', 201


def delayed_check(application):
    time.sleep(1200)  # 20 minets
    if check_available_page(application['url']):
        print('Error: page is available')
    else:
        if AppRepository().ban_app_by_bundle(application['bundle']):
            NotificationUsers().ban_application_notify(application)
            print(f"successfully banned: {application['bundle']}")


def check_available_page(url) -> bool:
    response = requests.head(url).status_code
    print(response)
    return str(response).startswith(("3", "2"))


if __name__ == '__main__':
    # app.run(threaded=True)
    http_server = WSGIServer(("0.0.0.0", 5020), app)
    http_server.serve_forever()
