from flask import Flask
from flask import request
from flask import render_template
from flask import make_response
import json

from main import connect, bot_message

app = Flask(__name__)
connect()

'''Voir main.py pour les clefs d'accès'''

@app.route("/", methods = ['GET'])
def start():
    return render_template('botMoodleUB.html')


@app.route("/update", methods = ['POST'])
def update():
    print(request.form)
    list_ret = bot_message(request.form["msg"])
    print(list_ret)
    print(json.dumps(list_ret))
    ret = make_response(json.dumps(list_ret), 200)
    ret.status_code = 200
    ret.headers['Access-Control-Allow-Origin'] = '*'
    return ret

if __name__ == "__main__":
    app.run(host="localhost")
