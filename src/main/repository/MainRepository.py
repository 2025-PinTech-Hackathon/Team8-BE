from sqlalchemy.orm import Session
from src.main.domain.model.Member import Member
from src.main.domain.model.Information import Information
from src.main.domain.model.Challenge import Challenge
from sqlalchemy import or_

class MainRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_member_by_id(self, member_id: str) -> Member | None:
        return self.db.query(Member).filter(Member.memberId == member_id).first()

    # 단일 태그 정보 조회 (tag는 한글 문자열로 들어옴, ex: "투자")
    def get_information_by_tag(self, tag: str):
        return self.db.query(Information).filter(
            Information.tags.contains([tag])
        ).all()

    # 다중 태그 정보 조회 (tags는 한글 문자열 리스트로 들어옴)
    def get_information_by_multiple_tags(self, tags: list[str]):
        return self.db.query(Information).filter(
            or_(*[Information.tags.contains([tag]) for tag in tags])
        ).all()
    
    # 맞춤형 챌린지 메인 페이지
    def get_challenges_by_tag(self, tags: list[str]):
        return self.db.query(Challenge).filter(
            or_(*[Challenge.chTags.contains([tag]) for tag in tags])
    ).all()
    
    # 태그 목록 조회
    def get_tags(self):
        # 사용자의 interest 필드에 있는 모든 태그 조회
        return self.db.query(Member.interest).distinct().all()[0][0]
