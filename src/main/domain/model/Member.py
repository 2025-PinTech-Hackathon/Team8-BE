from sqlalchemy import Column, String, Enum, Boolean
from sqlalchemy import Enum as SqlEnum
from src.main.domain.database import Base
from src.main.domain.model.MemberEnum import AgeGroupEnum, JobEnum, InterestEnum
from sqlalchemy.types import JSON
from sqlalchemy.orm import relationship
from src.main.domain.model.MemberChallengeRoom import member_challenge_room

class Member(Base):
    __tablename__ = "member"

    memberId = Column("member_id", String(36), primary_key=True, index=True)
    name = Column("name", String(100))
    email = Column("email", String(100))
    gender = Column("gender", Boolean)
    age = Column("age", SqlEnum(AgeGroupEnum, name="age"), nullable=False)
    job = Column("job", SqlEnum(JobEnum, name="job"), nullable=False)
    interest = Column("interest", JSON)   # 리스트 형태로 저장

    # ChallengeRoom과 N:M 관계 설정
    challengeRoom = relationship(
        "ChallengeRoom",
        secondary=member_challenge_room,
        back_populates="member"
    )

    # Check와 1:N 관계 설정
    checkTable = relationship("CheckTable", back_populates="member", cascade="all, delete-orphan")