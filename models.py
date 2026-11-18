from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):

    id = db.column(db.integer, primary_key=True)
    name = db.column(db.string(100))
    email = db.cloumn(db.string(100))