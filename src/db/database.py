from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base, sessionmaker
from sqlalchemy_utils import create_database, database_exists
from config import settings

DATABASE_URI = f'postgresql://{settings.db_username}:{settings.db_password}' \
    f'@{settings.db_host}:{settings.db_port}/{settings.db_name}'

# create the postgres database engine
engine = create_engine(DATABASE_URI)
if not database_exists(engine.url):
    create_database(engine.url)

print(f'Connected to database: {settings.db_name} at host: {settings.db_host}')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
