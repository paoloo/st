from flask import Flask
from flask import Response
import time
import os

app = Flask(__name__)
_jRet = lambda k: Response(k, mimetype="application/json")
_getE = lambda _k: os.environ[_k] if _k in os.environ else ''

@app.route("/")
def alpha():
    return _jRet('{"status":"OK"}')

@app.route("/delay/<value>")
def beta(value):
    time.sleep(int(value))
    return _jRet('{"status":"ok", "delay": %d}' % int(value))

@app.route("/version")
def gamma():
    return _jRet('{"version":1.2, "commit":"%s"}' % _getE('COMMIT'))

if __name__ == '__main__':
    app.run(debug=True)
