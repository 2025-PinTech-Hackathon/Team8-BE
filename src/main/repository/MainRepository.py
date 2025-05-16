from sqlalchemy.orm import Session
from src.main.domain.model.Member import Member
from src.main.domain.model.Information import Information
from src.main.domain.model.Challenge import Challenge

class MainRepository:
    def __init__(self, db: Session):
        self.db = db

    # 맞춤형 정보 메인 페이지
    def get_member_by_id(self, member_id: str):

        print(f"[Repository] get_member_by_id: {member_id}")

        return self.db.query(Member).filter(Member.memberId == member_id).first()
    
    def get_feeds_by_tag(self, tag: str):

        print(f"[Repository] get_feeds_by_tag: {tag}")

        return (
            self.db.query(Information)
            .filter(Information.tags.contains([tag]))
            .all()
        )
    
    # 맞춤형 챌린지 메인 페이지
    def get_challenges_by_tag(self, tag: str):

        print(f"[Repository] get_challenges_by_tag: {tag}")

        return (
            self.db.query(Challenge)
            .filter(Challenge.chTags.contains([tag]))
            .all()
        )
    
    # 태그 목록 조회
    def get_tags(self):
        # 사용자의 interest 필드에 있는 모든 태그 조회
        return self.db.query(Member.interest).distinct().all()[0][0]