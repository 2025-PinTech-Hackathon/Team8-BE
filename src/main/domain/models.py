from sqlalchemy import Column, BigInteger, String, Text, JSON, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Information(Base):
    __tablename__ = "information"
    
    information_id = Column(BigInteger, primary_key=True, autoincrement=True)
    title = Column(String(255))
    content = Column(Text)
    publisherName = Column(String(100))
    tags = Column(JSON)
    createdAt = Column(DateTime)
    updatedAt = Column(DateTime)
    redirectUrl = Column(String(255)) 