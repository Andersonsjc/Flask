# -*- coding: iso-8859-15 -*-
from flask import Flask
import pyodbc

app = Flask(__name__)
app.config.from_pyfile('config.py')

db = pyodbc.connect(app.config['DSN'])

from views import *

if __name__ == "__main__":
    #app.run(host='0.0.0.0', port=8080)
    app.run(debug=True)
