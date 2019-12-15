#!/usr/bin/python3
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sys import argv

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(argv[1], argv[2], argv[3]),
        echo=False)

    Base.metadata.create_all(engine)

    session = Session(engine)
    for city, state in session.query(City, State)\
            .filter(City.state_id == State.id)\
            .order_by(City.id).all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
