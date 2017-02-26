from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/enternew')
def enternew():
    return render_template('food.html')

@app.route('/addfood', methods=['POST'])
def addfood():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    try:
        name = request.form['name']
        calories = request.form['calories']
        cuisine = request.form['cuisine']
        is_vegetarian = request.form['is_vegetarian']
        is_gluten_free = request.form['is_gluten_free']
        cursor.execute('INSERT INTO foods (name, calories, cuisine, is_vegetarian, is_gluten_free) VALUES (?,?,?,?,?)', (name, calories, cuisine, is_vegetarian, is_gluten_free))   # executemany method (?)
        connection.commit()
        message = 'Record successfully added'
    except:
        connection.rollback()
        message = 'Error in insert operation'
    finally:
        return render_template('result.html', message=message)
        connection.close()

@app.route('/favorite')
def favorite():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM foods WHERE name = "Pizza"')
    favorite = cursor.fetchone()
    return render_template('favorite.html', message=favorite[0])
    connection.close()

@app.route('/search', methods=['GET'])
def search():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    try:
        usr_search = request.args['name'] # or request.args.get('name'), also returns a tuple
        cursor.execute('SELECT * FROM foods WHERE name IS ?', (usr_search,))
        return jsonify(cursor.fetchall())
    except:
        connection.rollback()
        return 'Item does not exist in our database'
    finally:
        connection.close()

@app.route('/drop')
def drop():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute('DROP TABLE foods')
    return 'dropped table'
    connection.close()




# >>export FLASK_APP=<Name>.py
# >>flask run
