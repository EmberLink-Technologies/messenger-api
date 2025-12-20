from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('postgresql+psycopg://postgres:postgres@localhost/messenger-api-db', echo=True)
Session = sessionmaker(engine, autoflush=False, autocommit=False)


def get_db():
    db = Session()
    try:
        yield db
        db.commit()
    except:
        db.rollback()
        raise
    finally:
        db.close()
