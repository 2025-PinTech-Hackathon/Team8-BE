#entity 역할 파일
from sqlalchemy import Column, String, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from database import Base

class ChallengeRoom(Base):
    __tablename__ = "challenge_rooms"

    room_id = Column(BIGINT(unsigned=True), primary_key=True, autoincrement=True)
    
    member_id = Column(BIGINT(unsigned=True), ForeignKey("members.member_id"), nullable=False)
    challenge_id = Column(BIGINT(unsigned=True), ForeignKey("challenges.challenge_id"), nullable=False)

    status = Column(String(20), nullable=False)
    start_date = Column(Date, nullable=True)
    end_date = Column(Date, nullable=True)

    # relationship(className, relationship)
    member = relationship("Member", back_populates="challenge_rooms")
    challenge = relationship("Challenge", back_populates="challenge_rooms")
    checks = relationship("Check", back_populates="challenge_room", cascade="all, delete-orphan")
    codes = relationship("ChallengeCode", back_populates="challenge_room", cascade="all, delete-orphan")