#!/usr/bin/python3

"""
Connect to a MySQL server running on localhost at port 3306
and lists all State objects from the database
hbtn_0e_6_usa where a certain letter is present in the state name
"""
from model_state import Base, State
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, password, db_name), pool_pre_ping=False)

    Session = sessionmaker(bind=engine)

    session = Session()
    Base.metadata.create_all(engine)

    letter = 'a'
    stato = session.query(State).filter(
        State.name.like('%a%')).order_by(
        State.id).all()
    for state in stato:
        print("{}: {}".format(state.id, state.name))
    session.close()
