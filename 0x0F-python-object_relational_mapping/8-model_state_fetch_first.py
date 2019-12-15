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
    data = session.query(State).order_by(State.id).first()
    if data:
        print("{}: {}".format(data.id, data.name))
    else:
        print("Nothing")
    session.close()
