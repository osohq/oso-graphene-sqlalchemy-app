"""Entrypoint to the expenses application"""
from flask import Flask
from flask_graphql import GraphQLView

from .models import db
from .schema import schema

from . import user
from . import sql

app = Flask(__name__)


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)

    app.config.from_mapping(
        SQLALCHEMY_DATABASE_URI='sqlite:///../expenses.db',
    )

    db.init_app(app)

    app.register_blueprint(user.bp)
    app.register_blueprint(sql.bp)

    return app


app = create_app()

app.add_url_rule('/graphql', view_func=GraphQLView.as_view(
    'graphql',
    schema=schema,
    graphiql=True))
