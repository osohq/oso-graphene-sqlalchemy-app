# oso: authorization as code with GraphQL [Graphene, SQLAlchemy Example]

oso allows you to write policy as code, tightly integrated
with application code, logic, and data, and provides a simple
way to enforce authorization on all requests.

This repository contains an example application discussed [on our
blog](https://www.osohq.com/post/graphql-authorization-graphene-sqlalchemy-oso).

## Install & Running

1. Install python requirements, using Python 3.

   ```
   pip install -r requirements.txt
   ```

2. Load fixture data.

   ```
   python -m app.fixtures
   ```

3. Run the app:

   ```
   $ FLASK_RUN_EXTRA_FILES=app/policy.polar FLASK_DEBUG=1 flask run
   ```

4. Visit http://localhost:5000/graphql and make some queries.
5. Go to http://localhost:5000/sql to see the SQL used in the prior
   query.
