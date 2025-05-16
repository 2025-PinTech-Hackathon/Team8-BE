from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from typing import Dict, Any

from src.main.auth.middlewares import get_current_user
from src.main.domain.database import get_db
from src.main.service.FeedService import FeedService

FeedAPIRouter = APIRouter(
    prefix="/feed",
    tags=["feed"]
)

@FeedAPIRouter.get("/finance/{feed_id}", response_model=Dict[str, Any])
async def get_finance_feed(
    feed_id: int,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
) -> Dict[str, Any]:
    print(f"[DEBUG] current_user: {current_user}")
    feed_service = FeedService(db)
    feed = feed_service.get_finance_feed_by_id(feed_id)
    
    return {
        "title": feed.title,
        "publisherName": feed.publisherName,
        "content": feed.content,
        "createdAt": feed.createdAt.strftime("%Y-%m-%d %H:%M:%S") if feed.createdAt else None,
        "updatedAt": feed.updatedAt.strftime("%Y-%m-%d %H:%M:%S") if feed.updatedAt else None
    }

