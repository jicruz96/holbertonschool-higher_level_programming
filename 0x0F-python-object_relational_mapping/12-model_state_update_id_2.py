#!/usr/bin/python3
"""
changes state.name for a State object with state.id = 2 from db
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker

if __name__ == "__main__":

    state_id_target = 2
    new_state_name = "New Mexico"
    user = argv[1]
    pw = argv[2]
    db = argv[3]
    URL = "mysql+mysqldb://{}:{}@localhost/{}".format(user, pw, db)

    engine = create_engine(URL)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    for state in session.query(State).filter(State.id == state_id_target):
        state.name = new_state_name
    session.commit()
    session.close()
