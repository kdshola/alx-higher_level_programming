#!/usr/bin/python3
""" listState object from the database hbtn_0e_6_usa from given argument
a take 4 arguments: mysql username, mysql password, database name and
state name to search
"""

from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sys import argv
if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    column = session.query(State).filter(State.name == (argv[4],))
    try:
        print(column[0].id)
    except IndexError:
        print("Not found")
