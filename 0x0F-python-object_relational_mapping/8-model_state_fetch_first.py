#!/usr/bin/python3
""" prints the first State object from the database hbtn_0e_6_usa """

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
        state = session.query(State).first()
        if state is None:
            print("Nothing")
        else:
            print("{}: {}".format(state.id, state.name))
        session.close()
    except:
        pass
