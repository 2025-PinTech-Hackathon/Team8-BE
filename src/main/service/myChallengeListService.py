#userId랑 tag랑 status를 불러와서
#Member에서 userId를 통해 이름과 challegeList를 받아올 예정인데
#여기서 status와 tag에 맞는 challenge만 골라서 Mapping 
#이후에 dto에 정보 넣어서 보내주면 됨

from typing import Optional


class myChallengeListService:
    async def get_my_challenge_List(user_id:str, tag: Optional[str], status: Optional[str]):
        #먼저 유저 정보 불러오기
        