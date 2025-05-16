from sqlalchemy.orm import Session
from src.main.domain.model.Member import Member
from src.main.domain.model.Information import Information
class MainRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_member_by_id(self, member_id: str):
        return self.db.query(Member).filter(Member.memberId == member_id).first()
    
    def get_feeds_by_tag(self, tag: str):
        return (
            self.db.query(Information)
            .filter(Information.tags.contains([tag]))
            .all()
        )