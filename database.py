import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_db(app):
    database_folder = os.path.join(app.root_path, "database")
    os.makedirs(database_folder, exist_ok=True)

    database_path = os.path.join(database_folder, "expenses.db")

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()