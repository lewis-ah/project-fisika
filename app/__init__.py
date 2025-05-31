from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'rahasia'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fisika.db'
    db.init_app(app)

    from .routes.materi_routes import materi_bp
    app.register_blueprint(materi_bp)

    with app.app_context():
        db.create_all()

    return app
