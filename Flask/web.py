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
    return render_template('index.html')


@app.route("/update", methods = ['POST'])
def update():
    print(request.form)
    list_ret = bot_message(request.form["msg"])
    print(list_ret["output"]["generic"])
    print(list_ret["context"]["skills"]["main skill"]["user_defined"])
    infos = {"msg" : list_ret["output"]["generic"],
             "context" : list_ret["context"]["skills"]["main skill"]["user_defined"] }
    print(json.dumps(infos))
    ret = make_response(json.dumps(infos), 200)
    ret.status_code = 200
    ret.headers['Access-Control-Allow-Origin'] = '*'
    return ret

if __name__ == "__main__":
    app.run(host="127.0.0.1")
