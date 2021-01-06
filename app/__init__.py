"""Entrypoint to the expenses application"""
from pathlib import Path

from flask import Flask, request
from flask_graphql import GraphQLView

from oso import Oso
from sqlalchemy_oso import register_models

from .models import db
from .schema import schema

from . import user
from . import sql

app = Flask(__name__)

CUSTOM_POLICY = ''

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

@app.route("/policy", methods=["GET"])
def get_policy():
    return CUSTOM_POLICY

@app.route("/policy", methods=["POST"])
def set_policy():
    global CUSTOM_POLICY

    # TODO: add policy check for who is allowed to edit policy
    policy = request.data.decode('ascii')
    CUSTOM_POLICY = policy
    return f"Updated to {CUSTOM_POLICY}"


@app.before_request
def setup_oso():
    oso = Oso()
    register_models(oso, db.Model)

    oso.load_file(Path(__file__).parent / "policy.polar")
    oso.load_file(Path(__file__).parent / "base.polar", scope="base")

    oso.load_file(Path(__file__).parent / "custom.polar", scope="custom")

    request.oso = oso