from flask import Flask
from flask import Response
import time

app = Flask(__name__)

@app.route("/")
def alpha():
    return Response('{"status":"OK"}', mimetype="application/json")

@app.route("/sleep/<value>")
def beta(value):
    time.sleep(int(value))
    return Response('{"status":"ok", "delay": %d}' % int(value), mimetype="application/json")

if __name__ == '__main__':
    app.run(debug=True)
