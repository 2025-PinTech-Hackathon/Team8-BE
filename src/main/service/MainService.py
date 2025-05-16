from src.main.repository.MainRepository import MainRepository
from src.main.domain.dto.InformationResponseDto import UserInformationResponse, Feed
from sqlalchemy.orm import Session
from src.main.domain.dto.ChallengeResponseDto import UserChallengeResponse, ChallengeResponseDto

class MainService:
    def __init__(self, db: Session):
        self.repository = MainRepository(db)
    
    def get_information_by_tag(self, member_id: str, tag: str) -> UserInformationResponse:
        print("member_id (get_information_by_tag):", member_id)
        
        member = self.repository.get_member_by_id(member_id)

        if not member or tag not in member.interest:
            return None
        
        feeds = self.repository.get_feeds_by_tag(tag)

        print("feeds:", feeds)

        return UserInformationResponse(
            memberId=member.memberId,
            userName=member.name,
            categories=member.interest,
            feeds=[
                Feed(title=feed.title or "", content=feed.content or "", tag=tag) for feed in feeds
            ]
        )
    
    def get_challenge_by_tag(self, member_id: str, tag: str) -> UserChallengeResponse:
        member = self.repository.get_member_by_id(member_id)
        if not member or tag not in member.interest:
            return None
        
        challenges = self.repository.get_challenges_by_tag(tag)
        return UserChallengeResponse(
            userName=member.name,
            categories=member.interest,
            challenges=[
                ChallengeResponseDto(
                    title=challenge.title,
                    description=challenge.content,
                    tag=tag
                )
                for challenge in challenges
            ]
        )
