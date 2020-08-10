#!/usr/bin/python3
""" prints all City objects from db """

from sys import argv
from model_state import Base, State
from model_city import City
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

    for city, state in session\
            .query(City, State).filter(State.id == City.state_id):
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
