from flask import current_app, g, request, Blueprint
from werkzeug.exceptions import Unauthorized

from sqlalchemy.orm import Session

from .models import User, db

bp = Blueprint("user", __name__)


class Actor:
    """base abstract user type"""
    pass


class Guest:
    """Anonymous user."""
    def __str__(self):
        return "Guest"


@bp.before_app_request
def set_current_user():
    """Set the `current_user` from the authorization header (if present)"""
    if "current_user" not in g:
        # NOTE: User defaults to alice so that using this demo is easy!
        # Don't do this in a real application!
        email = request.headers.get("user", "alice@foo.com")
        if email:
            try:
                # Use non authenticated session to get the current user.
                session = Session(bind=db.engine)
                g.current_user = session.query(
                    User
                ).filter(User.email == email).first()
            except Exception as e:
                current_app.logger.exception(e)
                return Unauthorized("user not found")
        else:
            g.current_user = Guest()
