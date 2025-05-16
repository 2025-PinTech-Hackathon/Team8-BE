from sqlalchemy import Column, String, DateTime, Enum, Text, BigInteger
from sqlalchemy import Enum as SqlEnum
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.types import JSON
from src.main.domain.database import Base
from src.main.domain.model.MemberEnum import InterestEnum

class Information(Base):
    __tablename__ = "information"

    informationId = Column("information_id", BigInteger, primary_key=True, index=True, autoincrement=True)
    title = Column(String(255))
    content = Column(Text)
    publisherName = Column(String(100))
    tags = Column("tags", JSON)   # 리스트 형태로 저장
    createdAt = Column(DateTime)
    updatedAt = Column(DateTime)
    redirectUrl = Column(String(255))