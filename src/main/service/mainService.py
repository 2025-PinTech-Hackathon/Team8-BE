from src.main.repository.MainRepository import MainRepository
from src.main.domain.dto.InformationResponseDto import MemberInformationResponse, Feed

class MainService:
    def __init__(self):
        self.repository = MainRepository()
    
    def get_information_by_category(self, category: str) -> MemberInformationResponse:
        member = self.repository.get_member()
        if not member or category not in member["categories"]:
            return None
        
        feeds = self.repository.get_feeds_by_category(category)
        return MemberInformationResponse(
            memberId = member["memberId"],
            memberName = member["memberName"],
            categories = member["categories"],
            feeds = [Feed(**feed) for feed in feeds]
        )