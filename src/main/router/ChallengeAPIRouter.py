from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Dict, Any

from src.main.auth.middlewares import get_current_user
from src.main.domain.database import get_db
from src.main.service.ChallengeService import ChallengeService

ChallengeAPIRouter = APIRouter(
    prefix="/feed",
    tags=["challenge"]
)

@ChallengeAPIRouter.get("/challenge/{challenge_id}", response_model=Dict[str, Any])
async def get_challenge(
    challenge_id: int,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
) -> Dict[str, Any]:
    try:
        challenge_service = ChallengeService(db)
        challenge = challenge_service.get_challenge_by_id(challenge_id)
        
        return {
            "title": challenge.title,
            "content": challenge.content
        }
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 