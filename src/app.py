from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from src.main.domain.database import Base, engine
from src.router import router
from contextlib import asynccontextmanager

# 모든 엔티티 import
from src.main.domain.model import (
    Member,
    Challenge,
    ChallengeRoom,
    CodeTable,
    CheckTable,
    Information,
    MemberChallengeRoom
)

load_dotenv()

origins = [
    "https://d2iyjdgwp264p6.cloudfront.net",
    "https://localhost:5173",
    "http://localhost:5173",
]

@asynccontextmanager
async def lifespan(app: FastAPI):
    # 앱 시작 시 테이블 생성
    Base.metadata.create_all(bind=engine)
    print("All tables created successfully.")
    yield

app = FastAPI(  
    title="fintory-server",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)


# 테이블 생성
def create_tables():
    Base.metadata.create_all(bind=engine)
    print("All tables created successfully.")

if __name__ == "__main__":
    create_tables()