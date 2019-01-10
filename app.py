from flask import Flask
from flask import Response
import time

app = Flask(__name__)
jR = lambda k: Response(k, mimetype="application/json")

@app.route("/")
def alpha():
    return jR('{"status":"OK"}')

@app.route("/delay/<value>")
def beta(value):
    time.sleep(int(value))
    return jR('{"status":"ok", "delay": %d}' % int(value))

@app.route("/version")
def gamma():
    return jR('{"version":1.1}')

if __name__ == '__main__':
    app.run(debug=True)
