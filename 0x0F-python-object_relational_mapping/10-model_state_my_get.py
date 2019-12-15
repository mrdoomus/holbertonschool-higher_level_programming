#!/usr/bin/python3
from model_state import Base, State
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
    data = session.query(State)\
        .filter(State.name == argv[4]).first()
    if data:
        print("{}".format(data.id))
    else:
        print("Not found")
    session.close()
