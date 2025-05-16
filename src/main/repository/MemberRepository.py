from sqlalchemy.orm import Session
from src.main.domain.model.Member import Member

class MemberRepository:
    def __init__(self, db: Session):
        self.db = db

    def find_by_id(self, memberId: str) -> Member | None:
        return self.db.query(Member).filter(Member.memberId == memberId).first()

    def save(self, member: Member) -> Member:
        self.db.add(member)
        self.db.commit()
        self.db.refresh(member)
        return member 