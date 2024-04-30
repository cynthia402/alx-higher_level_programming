#!/usr/bin/python3
"""add state and print its id """
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    session = Session()

    state_name = 'Louisiana'

    add_state = State(name=state_name)

    session.add(add_state)
    session.commit()

    see_states = session.query(State).filter(State.name == state_name)

    try:
        print(see_states[0].id)
    except IndexError:
        pass
