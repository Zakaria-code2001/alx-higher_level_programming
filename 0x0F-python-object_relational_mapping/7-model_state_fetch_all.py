#!/usr/bin/python3

"""
Connect to a MySQL server running on localhost at port 3306
and lists all State objects from the database hbtn_0e_6_usa
"""
from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Ensure all required arguments are provided
    if len(argv) != 4:
        print("Usage: ./7-model_state_fetch_all.py\
              <username> <password> <database_name>")
        exit(1)

    # Establishing the connection
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    # Creating metadata
    Base.metadata.create_all(engine)

    # Creating a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Querying and printing State objects
    states = session.query(State).order_by(State.id).all()
    if states:
        for state in states:
            print("{}: {}".format(state.id, state.name))
    else:
        print("No states found")

    # Closing the session
    session.close()
