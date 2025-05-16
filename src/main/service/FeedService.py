from sqlalchemy.orm import Session
from src.main.domain.models import Information
from src.main.repository.InformationRepository import InformationRepository
from fastapi import HTTPException

class FeedService:
    def __init__(self, db: Session):
        self.db = db
        self.information_repository = InformationRepository(db)
    
    def get_finance_feed_by_id(self, feed_id: int) -> Information:
        print(f"[DEBUG] feed_id: {feed_id}")
        feed = self.information_repository.find_by_id(feed_id)
        print(f"[DEBUG] feed: {feed}")
        
        if not feed:
            raise HTTPException(status_code=404, detail="Feed not found")
            
        return feed
