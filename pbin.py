from flask import Flask, render_template, redirect, url_for, request, abort
from flask.ext.sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)

class Paste(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text())

    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return '<Paste {0}>'.format(self.id)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add():
    p = Paste(request.form['text'])
    db.session.add(p)
    db.session.commit()
    return redirect(url_for('paste', id=p.id))

@app.route('/<int:id>')
def paste(id):
    p = Paste.query.get(id)
    if p is None:
        return abort(404)
    return render_template('paste.html', paste=p)
