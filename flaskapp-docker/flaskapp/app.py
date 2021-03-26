from flask import Flask, render_template, jsonify
import os

from db.database import db
from models import User

def init_app():
    """Initialises the application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config['SECRET_KEY'] = 'APP_SECRET_KEY'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Kati8212579!@my-database.cvgmzutcx9w8.eu-west-1.rds.amazonaws.com/postgres'
    db.init_app(app=app)
    return app


app = init_app()

@app.route('/health')
def health():
    """An endpoint showing the health of the app."""
    return render_template('home.html')

@app.route('/user/<name>/<email>')
def add_user(name, email):
    db.session.add(User(username=name, email=email))
    db.session.commit()

    return jsonify({'message': 'user is added.'})

