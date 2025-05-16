from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
from typing import Generator
from sqlalchemy.orm import Session

load_dotenv()  # .env 파일 로드

# 환경 변수 사용
fintory_mysql_url = os.getenv("FINTORY_MYSQL_URL")
fintory_mysql_port = os.getenv("FINTORY_MYSQL_PORT")
fintory_mysql_user = os.getenv("FINTORY_MYSQL_USERNAME")
fintory_mysql_password = os.getenv("FINTORY_MYSQL_PASSWORD")
fintory_mysql_database = os.getenv("FINTORY_MYSQL_DB")
database_url = f"mysql+pymysql://{fintory_mysql_user}:{fintory_mysql_password}@{fintory_mysql_url}:{fintory_mysql_port}/{fintory_mysql_database}?charset=utf8mb4"

engine = create_engine(database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

Base.metadata.schema = "fintory"

def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()