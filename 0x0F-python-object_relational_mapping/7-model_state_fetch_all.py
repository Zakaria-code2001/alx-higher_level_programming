#!/usr/bin/python3

"""
Connect to a MySQL server running on localhost at port 3306
and lists all State objects from the database hbtn_0e_6_usa
"""
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State

db_url = "mysql+mysqldb://root:root@localhost:3306/my_db"
engine = create_engine(db_url, pool_pre_ping=True)

Session = sessionmaker(bind=engine)
session = Session()

for state in session.query(State).order_by(State.id).all():
    print(f"{state.id}: {state.name}")

session.close()
