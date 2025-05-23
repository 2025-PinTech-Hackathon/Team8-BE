from sqlalchemy import Column, Integer, String, ForeignKey, BigInteger
from sqlalchemy import Enum as SqlEnum
from src.main.domain.database import Base
from sqlalchemy.orm import relationship

class CodeTable(Base):
    __tablename__ = "code_table"

    codeId = Column("code_id", BigInteger, primary_key=True, autoincrement=True, index=True)
    roomId = Column("room_id", BigInteger, ForeignKey("challenge_room.room_id"), unique=True)
    code = Column(String(6))

    # ChallengeRoom과 1:1 관계
    challengeRoom = relationship("ChallengeRoom", back_populates="codeTable")