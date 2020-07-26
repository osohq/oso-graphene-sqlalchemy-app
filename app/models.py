from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.orm import relationship

db = SQLAlchemy()


class Expense(db.Model):
    __tablename__ = 'expenses'

    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer)

    created_by_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_by = relationship("User")

    description = db.Column(db.Text)


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(256))
