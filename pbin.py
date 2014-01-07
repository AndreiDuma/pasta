import os

from flask import Flask, render_template, redirect, url_for
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)

app.debug = True

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/paste', methods=['POST'])
def paste():
    return redirect(url_for('index'))
