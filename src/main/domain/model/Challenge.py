from sqlalchemy import Column, BigInteger, String
from sqlalchemy.types import JSON
from src.main.domain.database import Base
from src.main.domain.model.MemberEnum import InterestEnum
from sqlalchemy.orm import relationship
from typing import List

class Challenge(Base):
    __tablename__ = "challenge"

    challengeId = Column("challenge_id", BigInteger, primary_key=True, autoincrement=True, index=True)
    title = Column(String(255))
    content = Column(String(3000))
    chTags = Column("ch_tags", JSON) # 리스트 형태로 저장

    # ChallengeRoom과 1:N 관계 설정
    challengeRoom = relationship("ChallengeRoom", back_populates="challenge", cascade="all, delete-orphan")