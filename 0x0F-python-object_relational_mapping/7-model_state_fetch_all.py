#!/usr/bin/python3

"""
Connect to a MySQL server running on localhost at port 3306
and lists all State objects from the database hbtn_0e_6_usa
"""
from model_state import Base, State
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


db_url = "mysql+mysqldb://root:root@localhost:3306/hbtn_0e_6_usa"
engine = create_engine(db_url, pool_pre_ping=False)

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, password, db_name), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    session = Session()
    Base.metadata.create_all(engine)

    stato = session.query(State).order_by(State.id).all()
    for state in stato:
        print("{}: {}".format(state.id, state.name))
    session.close()
