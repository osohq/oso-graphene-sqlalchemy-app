from sqlalchemy.orm import Session

from .models import User, Expense, Project


def load_fixtures(session):
    alice = User(email="alice@foo.com")
    bob = User(email="bob@foo.com")
    jim = User(email="jim@bar.com")

    office_supplies = Project(name="Office supplies", created_by=bob, users=[alice])
    furniture = Project(name="furniture", created_by=alice, users=[alice, bob])

    pencils = Expense(amount=10, description="#2 HB", created_by=alice, project=office_supplies)
    pens = Expense(amount=5, description="Blue ink", created_by=bob, project=office_supplies)
    desk = Expense(amount=100, description="New desk", created_by=alice, project=furniture)
    chair = Expense(amount=150, description="Chair", created_by=jim, project=furniture)

    session.add_all([alice, bob, jim, pencils, pens, desk, chair, office_supplies, furniture])
    session.commit()


if __name__ == '__main__':
    from . import app
    from .models import db

    with app.app_context():
        db.create_all()
        session = Session(bind=db.get_engine())
        load_fixtures(session)
