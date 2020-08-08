#!/usr/bin/python3
"""Start link class to table in database 
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    user = sys.argv[1]
    passsword = sys.argv[2]
    database = sys.argv[3]
    str = 'mysql+mysqldb://{}:{}@localhost/{}'
    engine_str = str.format(user, passsword, database)
    engine = create_engine(engine_str, pool_pre_ping=True)
    Base.metadata.create_all(engine)
