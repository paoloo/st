from flask import Flask
from flask import Response
import resource
import time
import os

app = Flask(__name__)
_jRet = lambda _k: Response(_k, mimetype="application/json")
_getE = lambda _k: os.environ[_k] if _k in os.environ else ''

@app.route("/")
def alpha():
    return _jRet('{"status":"ok"}')

@app.route("/delay/<value>")
def beta(value):
    time.sleep(int(value))
    return _jRet('{"status":"ok", "delay": %d}' % int(value))

@app.route("/version")
def gamma():
    return _jRet('{"status":"ok", "version":1.3, "commit":"%s"}' % _getE('COMMIT'))

@app.route("/ulimits")
def delta():
    _soft, _hard = resource.getrlimit(resource.RLIMIT_NOFILE)
    return _jRet('{"status":"ok", "limits": {"soft":"%s", "hard":"%s"}}' % (_soft, _hard))

@app.errorhandler(404)
def page_not_found(e):
    return _jRet('{"status":"error"}'), 404

if __name__ == '__main__':
    app.run(debug=True)
