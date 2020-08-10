#!/usr/bin/python3
""" lists all State objects that contain the letter a """

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy import func

if __name__ == "__main__":
    user = argv[1]
    pw = argv[2]
    db = argv[3]
    URL = "mysql+mysqldb://{}:{}@localhost/{}".format(user, pw, db)

    engine = create_engine(URL)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State)
    states = states.filter(State.name.like('%a%'))
    for state in states:
        session.delete(state)
    session.commit()
    session.close()
