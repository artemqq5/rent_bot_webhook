from gevent.pywsgi import WSGIServer

from flask import Flask, request

app = Flask(__name__)


@app.route("/flows", methods=['GET'])
def web_handler():
    id_ = request.args.get("flow_id")



    return 'OK', 200


if __name__ == '__main__':
    app.run()
    # http_server = WSGIServer(("0.0.0.0", 5010), app)
    # http_server.serve_forever()
