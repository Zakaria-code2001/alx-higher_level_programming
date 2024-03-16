#!/usr/bin/python3

"""
Connect to a MySQL server running on localhost at port 3306
and lists all State objects from the database hbtn_0e_6_usa
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
        State.name.like(f'%{letter}%')).order_by(
        State.id).first()
    if stato:
        print("{}: {}".format(stato.id, stato.name))
    else:
        print("Nothing")
    session.close()
