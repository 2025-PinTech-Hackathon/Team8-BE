from sqlalchemy import Table, Column, String, ForeignKey, BigInteger
from sqlalchemy import Enum as SqlEnum
from src.main.domain.database import Base

member_challenge_room = Table(
    "member_challenge_room",
    Base.metadata,
    Column("member_id", String(36), ForeignKey("member.member_id"), primary_key=True),
    Column("room_id", BigInteger, ForeignKey("challenge_room.room_id"), primary_key=True)
)