from flask import Flask, render_template
from time import strftime, localtime
import redis
import json

app = Flask(__name__)
rd = redis.Redis(host='localhost', port=6379, db=0)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/increment', methods=['POST'])
def increment():
    incr = rd.incr('incr')
    return json.dumps({'clicks': incr})

@app.route('/lastvalue', methods=['GET'])
def lastvalue():
    rd.decr('incr')
    incr = rd.incr('incr')
    return json.dumps({'clicks': incr})


if __name__ == "__main__":
    app.run(debug=True)