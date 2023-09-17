#!/usr/bin/python3
"""
A script to create the State “California” with
the City “San Francisco” in the database.
"""

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]

    engine = create_engine(
            f'mysql+mysqldb://{username}:{password}@localhost/{database_name}',
            pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    california = State(name='California')
    san_francisco = City(name='San Francisco')
    california.cities.append(san_francisco)

    session.add(california)
    session.commit()
    session.close()
