from sqlalchemy import Column, String, DateTime, Enum
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.types import JSON
from src.main.domain.database import Base
from src.main.domain.model.MemberEnum import InterestEnum

class Information(Base):
    __tablename__ = "information"

    informationId = Column(String, primary_key=True, index=True)
    title = Column(String(255))
    content = Column(LONGTEXT)
    publisherName = Column(String(100))
    tags = Column("tags", JSON)   # 리스트 형태로 저장
    createdAt = Column(DateTime)
    updatedAt = Column(DateTime)
    redirectUrl = Column(String(255))