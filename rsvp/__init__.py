import os
from flask import Flask, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# Setup ORM
from rsvp.models import Base
engine = create_engine(os.environ.get('ENGINE'))
Base.metadata.create_all(engine)
Session = scoped_session(
    sessionmaker(bind=engine),
    scopefunc=lambda: request)


# Setup Web App
app = Flask(__name__)
app.debug = True
app.secret_key = os.environ.get('SECRET_KEY')
from rsvp.routes import app

@app.teardown_request
def teardown_request(exception):
    print str(exception)
    Session.remove()


if __name__ == '__main__':
    app.run()
