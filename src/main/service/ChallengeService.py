from sqlalchemy.orm import Session
from src.main.domain.model.Challenge import Challenge

class ChallengeService:
    def __init__(self, db: Session):
        self.db = db
        
    def get_challenge_by_id(self, challenge_id: int) -> Challenge:
        challenge = self.db.query(Challenge).filter(Challenge.challengeId == challenge_id).first()
        if not challenge:
            raise ValueError(f"Challenge with id {challenge_id} not found")
        return challenge 