#entity 역할 파일
<<<<<<< HEAD
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
=======
from sqlalchemy import Column, String, DateTime, ForeignKey, BigInteger, SqlEnum, Date, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from database import Base
from src.main.domain.model.ChallengeStatusEnum import ChallengeStatusEnum

class ChallengeRoom(Base):
    __tablename__ = "challenge_room"

    roomId = Column("room_id", BigInteger, primary_key=True, index=True, autoincrement=True)
    memberId = Column("member_id", String, ForeignKey("member.member_id"), nullable=False)
    challengeId = Column("challenge_id", BigInteger(unsigned=True), ForeignKey("challenge.challenge_id"), nullable=False)
    status = Column(SqlEnum(ChallengeStatusEnum, name="challenge_status"), nullable=False)
    startDate = Column("start_date", Date, nullable=True)
    endDate = Column("end_date", Date, nullable=True)
    participants = Column("participants", Integer, nullable=True)

    member = relationship(
        "Member",
        secondary="member_challenge_room",
        back_populates="challengeRoom"
    )

    # Code와 1:1 관계 설정
    code = relationship("Code", useList=False, back_populates="challengeRoom")

    # Challenge와 N:1 관계
    challenge = relationship("Challenge", back_populates="challengeRoom")

     # Check와 1:N 관계
    check = relationship("Check", back_populates="challengeRoom", cascade="all, delete-orphan")
>>>>>>> 1b00445e0c24a2e451f981345beaf0cb4d7ba9e4
