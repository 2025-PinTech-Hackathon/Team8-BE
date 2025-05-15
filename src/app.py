from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from src.router import router


load_dotenv()

origins = [
    "https://d2iyjdgwp264p6.cloudfront.net",
    "https://localhost:5173",
    "http://localhost:5173",
]


app = FastAPI(  
    title="fintory-server",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)