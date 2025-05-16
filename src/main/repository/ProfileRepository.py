from sqlalchemy.orm import Session
from src.main.domain.model.Member import Member

class ProfileRepository:
    def __init__(self, db: Session):
        self.db = db

    def find_by_name(self, name: str) -> Member | None:
        return self.db.query(Member).filter(Member.name == name).first()
    
    def find_by_member_id(self, member_id: str) -> Member | None:
        return self.db.query(Member).filter(Member.memberId == member_id).first()
    
    def create_member(self, member: Member) -> Member:
        self.db.add(member)
        self.db.commit()
        self.db.refresh(member)
        return member