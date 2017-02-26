import sqlite3

connection = sqlite3.connect('database.db') # look for a file. If it doesn't exist, create one.
print ('We\'re connected!')

connection.execute('CREATE TABLE friends (name TEXT, age INTEGER)')
print ('Table created!')

connection.close()
