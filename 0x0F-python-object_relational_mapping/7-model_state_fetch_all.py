#!/usr/bin/python3
"""This module lists all State objects from the database hbtn_0e_6_usa"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    try:
        user = argv[1]
        pw = argv[2]
        db = argv[3]
        URL = "mysql+mysqldb://{}:{}@localhost/{}".format(user, pw, db)
        engine = create_engine(URL)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        states = session.query(State)
        for state in states:
            print("{}: {}".format(state.id, state.name))
        session.close()
    except:
        pass
