from sqlalchemy import Table, Column, String, ForeignKey, BigInteger
from sqlalchemy import Enum as SqlEnum
from sqlalchemy.orm import relationship
from src.main.domain.database import Base


class MemberChallengeRoom(Base):
    __tablename__ = "member_challenge_room"

    memberId=Column("member_id", String(36), ForeignKey("member.member_id"), primary_key=True)
    roomId=Column("room_id", BigInteger, ForeignKey("challenge_room.room_id"), primary_key=True)

    member = relationship("Member", back_populates="member_challenge_room")
    room = relationship("ChallengeRoom", back_populates="member_challenge_room")


# member_challenge_room = Table(
#     "member_challenge_room",
#     Base.metadata,
#     Column("member_id", String(36), ForeignKey("member.member_id"), primary_key=True),
#     Column("room_id", BigInteger, ForeignKey("challenge_room.room_id"), primary_key=True)
# )