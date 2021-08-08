#!/usr/bin/python3
"""
    Script that lists all State objects from the database
"""
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from sqlalchemy.orm import relationship
from relationship_city import Base, City
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
    # Printing states with all the cities.
    new_element = cities(State.name("California"), City.name("San Francisco"))
    session.commit()
    session.close()
