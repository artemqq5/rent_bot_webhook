from gevent.pywsgi import WSGIServer

from flask import Flask, request

from data.repository.AppRepository import AppRepository
from domain.notify.NotificationUsers import NotificationUsers

app = Flask(__name__)


@app.route("/flows", methods=['GET'])
def web_handler():
    id_ = request.args.get("flow_id")
    application = AppRepository().get_app_by_id(id_)

    if not application:
        return 'OK', 200

    if not AppRepository().ban_app_by_id(id_):
        return 'OK', 200

    NotificationUsers().ban_application_notify(application)

    return 'OK', 200


if __name__ == '__main__':
    app.run()
    # http_server = WSGIServer(("0.0.0.0", 5010), app)
    # http_server.serve_forever()
