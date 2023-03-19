#!/usr/bin/python3
"""the script that changes the name of the state object from
the database hbtn_0e_6_usa"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy import asc


if __name__ == "__main""__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhosrt/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    start = sessionmaker()
    start.configure(bind=engine)
    session = start()
    stmt = session.quey(State).filter_by(id=2)
    for i in stmt:
        i.name = "New Mexico"
    session.commit()
    session.close()
