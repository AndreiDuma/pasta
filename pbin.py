import os

from flask import Flask, render_template, redirect, url_for
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)

app.debug = True

class Paste(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text())

    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return '<Paste %s>' % self.id

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add():
    p = Paste(request.form['text'])
    db.session.add(p)
    db.session.commit()
    return redirect(url_for('paste'), id=p.id)

@app.route('/p/<int:id>')
def paste():
    p = Paste.query.get(id)
    if p is None:
        return abort(404)
    return p.text
