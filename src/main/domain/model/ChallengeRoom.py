#entity 역할 파일
from sqlalchemy import Column, String, Enum, BigInteger, ForeignKey, Date, Integer
from sqlalchemy import Enum as SqlEnum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from src.main.domain.database import Base
from src.main.domain.model.ChallengeStatusEnum import ChallengeStatusEnum
from src.main.domain.model._MemberChallengeRoom import MemberChallengeRoom


class ChallengeRoom(Base):
    __tablename__ = "challenge_room"

    roomId = Column("room_id", BigInteger, primary_key=True, index=True, autoincrement=True)
    #memberId = Column("member_id", String(36), ForeignKey("member.member_id"), nullable=False)
    challengeId = Column("challenge_id", BigInteger, ForeignKey("challenge.challenge_id"), nullable=False)
    status = Column(SqlEnum(ChallengeStatusEnum, name="challenge_status"), nullable=False)
    startDate = Column("start_date", Date, nullable=True)
    endDate = Column("end_date", Date, nullable=True)
    participants = Column("participants", Integer, nullable=True)

    # member = relationship(
    #     "Member",
    #     # secondary=member_challenge_room,
    #     back_populates="challengeRoom"
    # )

    # Code와 1:1 관계 설정
    codeTable = relationship("CodeTable", uselist=False, back_populates="challengeRoom")

    # Challenge와 N:1 관계
    challenge = relationship("Challenge", back_populates="challengeRoom")

    member_challenge_room = relationship("MemberChallengeRoom", back_populates="room")

    # Check와 1:N 관계
    checkTable = relationship("CheckTable", back_populates="challengeRoom", cascade="all, delete-orphan")