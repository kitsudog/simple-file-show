from flask import Flask
from redis import Redis
import os
app = Flask(__name__)
redis = Redis(host=os.environ.get('REDIS_HOST', 'redis'), port=6379)

def getPage(page=None,err="error"):
    if page is not None and os.path.exists("%s.html" % page):
        target=page
    else:
        target=err 
    with open("%s.html" % target, mode="r") as fin:
        return '\n'.join(fin.readlines())

@app.route('/<dir>/')
def hello(dir):
    if os.path.isdir(dir):
        return getPage(page="%s/%s" % (dir,redis.incr('hits_%s' % dir)),err="over")
    return getPage(err="none")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
