from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # Tworzymy obiekt db

def create_app():
    app = Flask(__name__)

    # Konfiguracja bazy danych
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/tasks.db'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://@todo-flask-server.database.windows.net:1433/tasksdb?driver=ODBC+Driver+17+for+SQL+Server&authentication=ActiveDirectoryMsi'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)  # Inicjalizujemy db z aplikacją

    from .routes import main
    app.register_blueprint(main)

    return app
