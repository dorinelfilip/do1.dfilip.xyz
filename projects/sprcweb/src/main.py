import string
import random

from flask import Flask
from flask import request
from flask import render_template
from flask import make_response

app = Flask(__name__)


def rand_generator(size=6, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/cache/<cid>")
def cache(cid):
    import datetime
    return 'ID={}\n Time={}'.format(cid, str(datetime.datetime.now()))

@app.route("/lab01")
def lab01():
    return render_template('lab01.html')

@app.route("/lab01-cookie")
def lab01_cookie():
	context = {'cookie_key': rand_generator(),
			   'cookie_value': rand_generator()
	          }
	resp = make_response(render_template('lab01-cookie.html', **context))
	resp.set_cookie(context['cookie_key'], context['cookie_value'])
	return resp



if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False, port=80)
