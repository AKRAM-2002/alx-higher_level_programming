#!/usr/bin/python3
"""
  lists all City objects from the database hbtn_0e_101_usa
  <city id>: <city name> -> <state name>
"""

if __name__ == "__main__":
    import sys
    from relationship_state import Base, State
    from relationship_city import Base, City

    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    if len(sys.argv)!= 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    
    Base.metadata.create_all(engine)

    
  
    Session = sessionmaker(bind=engine)
    session = Session()

    st = session.query(State).join(City).order_by(City.id).all()

    for state in st:
        for city in state.cities:
            print("{}: {} -> {}".format(city.id, city.name, state.name))

    session.close()