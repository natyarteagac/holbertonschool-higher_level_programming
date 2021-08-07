#!/usr/bin/python3
"""
    Script that lists all State objects from the database
"""
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import (create_engine)
from sys import argv

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(argv[1], argv[2],
                argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(engine)
    session = Session()
    # Choosing the first result of the query
    first = session.query(State).order_by(State.id).first()
    if not first:
        print("Nothing")
    else:
        print("{}: {}".format(first.id, first.name))
