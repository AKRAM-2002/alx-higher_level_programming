#!/usr/bin/python3
"""
    Prints the first State object from the database hbtn_0e_6_usa
"""


if __name__ == "__main__":
    import sys
    from model_state import Base, State

    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    if len(sys.argv)!= 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    
    Base.metadata.create_all(engine)

  
    Session = sessionmaker(bind=engine)
    session = Session()

    first_row = session.query(State).order_by(State.id).first()
    if(first_row is None):
        print("Nothing")
    else:
        print("{:d}: {:s}".format(first_row.id, first_row.name))

   
    session.close()