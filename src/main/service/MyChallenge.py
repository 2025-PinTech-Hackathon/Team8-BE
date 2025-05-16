from ast import List
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from typing import Optional

class MyChallenge:
    async def create_room(session: AsyncSession, challenge_id: int):
        