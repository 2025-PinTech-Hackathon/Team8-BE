from sqlalchemy import Column, BigInteger, Date, Boolean, ForeignKey, String
from sqlalchemy import Enum as SqlEnum
from src.main.domain.database import Base
from sqlalchemy.orm import relationship

class Check(Base):
    __tablename__ = "check"

    checkId = Column("check_id", BigInteger, primary_key=True, autoincrement=True, index=True)
    date = Column(Date)
    done = Column(Boolean)
    memberId = Column("member_id", String(36), ForeignKey("member.member_id"))
    roomId = Column("room_id", BigInteger, ForeignKey("challenge_room.room_id"))

    member = relationship("Member", back_populates="check")
    challengeRoom = relationship("ChallengeRoom", back_populates="check")