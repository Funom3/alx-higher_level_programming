#!/usr/bin/python3
"""A script that list all the state objects that contain the letter a
from the database hbtn_0e)6_usa"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy import asc

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    start = sessionmaker()
    start.configure(bind=engine)
    session = start()
    stmt = session.query(State).filter(
            State.name.like("%a%")).order_by(asc(State.id)).all()
    for i in stmt:
        print("{:d}: {:s}".format(i.id, i.id.name))
    session.close()
