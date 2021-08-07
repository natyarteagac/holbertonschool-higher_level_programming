#!/usr/bin/python3
"""
    Script that lists all State objects from the database
"""
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import Base, City
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
    for sql_state in session.query(State, City)\
        .join(State.id).join(State.name).join(City.id)\
        .join(City.name0).join(City.state_id)\
            .filter(State.id == City.state_id).\
            order_by(City.id).all():
        print(sql)
    session.close()
