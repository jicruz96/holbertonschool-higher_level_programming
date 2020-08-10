#!/usr/bin/python3
""" adds the State object “Louisiana” to db"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker

if __name__ == "__main__":
    try:
        user = argv[1]
        pw = argv[2]
        db = argv[3]
        URL = "mysql+mysqldb://{}:{}@localhost/{}".format(user, pw, db)

        engine = create_engine(URL)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()

        new_state_name = "Louisiana"
        new_state = State(new_state_name)
        session.add(new_state)
        session.commit()
        for state in session.query(State).filter(State.name == new_state_name):
            print(state.id)
        session.close()
    except:
        pass
