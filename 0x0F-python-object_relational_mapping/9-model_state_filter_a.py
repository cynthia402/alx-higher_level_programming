#!/usr/bin/python3
''' queries states where 'a' present in'''


import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    all_states = session.query(State).order_by(State.id)

    for obj in all_states:
        if 'a' in obj.name:
            print(obj.id, obj.name, sep=': ')
