from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()  # Tworzymy obiekt db

def create_app():
    app = Flask(__name__)

    # Konfiguracja bazy danych
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/tasks.db'
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///db.sqlite') #connection to database
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)  # Inicjalizujemy db z aplikacją

    from .routes import main
    app.register_blueprint(main)

    return app
