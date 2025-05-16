from sqlalchemy.orm import Session
from src.main.domain.model.Information import Information
from typing import Optional

class InformationRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def find_by_id(self, information_id: int) -> Optional[Information]:
        return self.db.query(Information).filter(Information.informationId == information_id).first() 