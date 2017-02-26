from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/birthday')
def birthday():
    return 'October 30 1911'

@app.route('/greeting/<name>')
def greeting(name):
    return 'Hello %s!' % name

@app.route('/add/<int:param1>/<int:param2>')
def add(param1, param2):
    summation = param1 + param2
    return 'The sum is %d' % summation

@app.route('/multiply/<int:param1>/<int:param2>')
def multiply(param1, param2):
    product = param1 * param2
    return 'The product is %d' % product

@app.route('/subtract/<int:param1>/<int:param2>')
def subtract(param1, param2):
    subtraction = param1 - param2
    return 'The difference is %d' % subtraction

@app.route('/favoritefoods')
def favoritefoods():
    foods = ['apples', 'bananas', 'pizza']
    return jsonify(foods)


# >>export FLASK_APP=<Name>.py
# >>flask run
