#!/usr/bin/python3
"""
  prints the State object with the state name passed as argument from the database hbtn_0e_6_usa
"""


if __name__ == "__main__":
    import sys
    import re
    from model_state import Base, State

    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    if len(sys.argv)!= 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    
    Base.metadata.create_all(engine)

    state_name = sys.argv[4]
    if (re.search('^[a-zA-Z ]+$', state_name) is None):
        print('Enter a valid name state (example: Texas)')
        exit(1)
  
    Session = sessionmaker(bind=engine)
    session = Session()

    

    state = session.query(State).filter(State.name == state_name).first()
    if(state is None):
        print("Not Found")
    else:
        print("{:d}".format(state.id))
    session.close()