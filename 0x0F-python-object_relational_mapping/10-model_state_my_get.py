#!/usr/bin/python3
""" prints the State object with the name passed as argument """

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker

if __name__ == "__main__":
    user = argv[1]
    pw = argv[2]
    db = argv[3]
    state_name = argv[4]
    URL = "mysql+mysqldb://{}:{}@localhost/{}".format(user, pw, db)

    engine = create_engine(URL)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    for state in session.query(State).filter(State.name == state_name):
        if state is None:
            print("Not found")
        else:
            print("{}".format(state.id))
    session.close()
