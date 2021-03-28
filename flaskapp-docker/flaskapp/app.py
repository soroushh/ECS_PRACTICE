from flask import Flask, render_template, jsonify
import os

from flaskapp.db.database import db
from flaskapp.models.models import User
from flaskapp.repos import get_user_repository
from flaskapp.services import get_user_service

def init_app():
    """Initialises the application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config['SECRET_KEY'] = 'APP_SECRET_KEY'
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
    db.init_app(app=app)
    return app


app = init_app()

@app.route('/health')
def health():
    """An endpoint showing the health of the app."""
    return render_template('home.html')

@app.route('/user/<name>/<email>')
def add_user(name, email):
    get_user_service().add_by_name_email(name=name, email=email)

    return jsonify({'message': 'user is added.'})

@app.route('/user/<name>')
def find_by_name(name):
    """."""
    user = get_user_repository().by_name(name=name)

    if user:
        return jsonify({'message': f'{user.email}'})
    else:
        return jsonify({'message': 'user not found.'})

