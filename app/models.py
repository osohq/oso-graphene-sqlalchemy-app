from flask import g, current_app, request
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.orm import relationship
from sqlalchemy import Table

from sqlalchemy_oso.flask import AuthorizedSQLAlchemy

db = AuthorizedSQLAlchemy(
    get_oso=lambda: current_app.oso,
    get_user=lambda: getattr(g, "current_user", None),
    get_action=lambda: "read"
)


class Expense(db.Model):
    __tablename__ = 'expenses'

    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer)

    created_by_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_by = relationship("User")

    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))
    project = relationship("Project", backref="expenses")

    description = db.Column(db.Text)


class Project(db.Model):
    __tablename__ = "projects"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)

    created_by_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_by = relationship("User")


user_project = db.Table(
    "user_project",
    db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('project_id', db.Integer, db.ForeignKey('projects.id'))
)


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(256))

    projects = relationship('Project', secondary=user_project,
                            backref="users")
