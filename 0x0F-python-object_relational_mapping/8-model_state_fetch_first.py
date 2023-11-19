#!/usr/bin/python3
"""  prints the first State object from the database hbtn_0e_6_usa
take 3 arguments: mysql username, mysql password and database name
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
    column = session.query(State).first()
    if column is None:
        print("Nothing")
    else:
        print(f"{column.id}: {column.name}")
