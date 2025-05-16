from sqlalchemy import Column, String, Enum, SqlEnum
from src.main.domain.database import Base
from src.main.domain.model.MemberEnum import AgeGroupEnum, JobEnum, InterestEnum
from sqlalchemy.types import JSON
from sqlalchemy.orm import relationship
from src.main.domain.model.MemberChallengeRoom import member_challenge_room

class Member(Base):
    __tablename__ = "member"

    memberId = Column(String, primary_key=True, index=True)
    name = Column(String(100))
    email = Column(String(100))
    gender = Column(bool)
    age = Column(SqlEnum(AgeGroupEnum, name="age"), nullable=False)
    job = Column(SqlEnum(JobEnum, name="job"), nullable=False)
    interest = Column("interest", JSON)   # 리스트 형태로 저장

    # ChallengeRoom과 N:M 관계 설정
    challengeRoom = relationship(
        "ChallengeRoom",
        secondary=member_challenge_room,
        back_populates="member"
    )

    # Check와 1:N 관계 설정
    check = relationship("Check", back_populates="member", cascade="all, delete-orphan")