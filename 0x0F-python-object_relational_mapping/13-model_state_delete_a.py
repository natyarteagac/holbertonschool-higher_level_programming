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
    # Deleting objects with the char a
    for objects in session.query(State).filter(State.name.like('%a%')).all():
        session.delete(objects)
        session.commit()
        session.close()
