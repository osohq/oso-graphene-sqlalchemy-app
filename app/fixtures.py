from .models import User, Expense
from sqlalchemy.orm import Session


def load_fixtures(session):
    alice = User(email="alice@foo.com")
    bob = User(email="bob@foo.com")
    jim = User(email="jim@bar.com")

    pencils = Expense(amount=10, description="#2 HB", created_by=alice)
    pens = Expense(amount=5, description="Blue ink", created_by=bob)
    desk = Expense(amount=100, description="New desk", created_by=alice)
    chair = Expense(amount=150, description="Chair", created_by=jim)

    session.add_all([alice, bob, jim, pencils, pens, desk, chair])
    session.commit()


if __name__ == '__main__':
    from . import app
    from .models import db

    with app.app_context():
        db.create_all()
        session = Session(bind=db.get_engine())
        load_fixtures(session)
