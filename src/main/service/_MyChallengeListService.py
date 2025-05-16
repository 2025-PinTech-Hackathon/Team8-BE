#userId랑 tag랑 status를 불러와서
#Member에서 userId를 통해 이름과 challegeList를 받아올 예정인데
#여기서 status와 tag에 맞는 challenge만 골라서 Mapping 
#이후에 dto에 정보 넣어서 보내주면 됨

from ast import List
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from typing import Optional

from src.main.domain.model.Member import Member
from src.main.domain.model.Challenge import Challenge
from src.main.domain.model.ChallengeRoom import ChallengeRoom
from src.main.domain.dto._MyChallengeListDto import MyChallengeSummaryDto

from src.main.repository.CheckRepository import CheckRepository
from src.main.repository.ChallengeRepository import ChallengeRepository
from src.main.repository.ChallengeRoomRepository import ChallengeRoomRepository
from src.main.repository.MemberChallengeRoomRepository import MemberChallengeRoomRepository
from src.main.repository.MemberRepository import MemberRepository
from src. main.domain.model.ChallengeStatusEnum import ChallengeStatusEnum
from src.main.domain.model.MemberEnum import InterestEnum
from src.main.domain.dto._MyChallengeListDto import MyChallengeListResDto

class MyChallengeListService:
    def get_my_challenge_List(session: AsyncSession, member_id:str,tag: Optional[str], status: str ):
        #먼저 유저 정보 불러오기
        member: Member = MemberRepository.get_by_member_id(session, member_id)
        
        if not member:
            raise HTTPException(status_code=404, detail="회원 정보를 찾을 수 없습니다.")

        # 2. 유저가 참여 중인 challengeRoom_id 목록 조회
        joined_room_ids = MemberChallengeRoomRepository.get_by_member_id(session,member_id)  # List[ChallengeRoom]

        
        if not joined_room_ids:
            raise HTTPException(status_code=404, detail="challengeID가 없습니다.")
        
        #print()
        # 2. 해당 room_id에 해당하는 ChallengeRoom 객체들 조회
        room_id_list = [item.roomId for item in joined_room_ids]
        rooms: List[ChallengeRoom] = ChallengeRoomRepository.get_by_room_id(session, room_id_list)
        
        if not joined_room_ids:
            raise HTTPException(status_code=404, detail="challengeRoom이 없습니다.")
        
        #MyChallengeSummaryDto하기
        myChallengeSummaryLists : List[MyChallengeSummaryDto] = []
        
        # ChallengeRoom 리스트를 순회
        for room in rooms:
            print(f"검사 중인 roomId: {room.roomId}, status: {room.status}")

            challenge: Challenge = ChallengeRepository.get_by_challenge_id(session, room.challengeId)
            print(f"challenge: {challenge}")

            if not challenge:
                raise HTTPException(status_code=404, detail="challenge가 없습니다.")
            progress = CheckRepository.get_progress(session, member_id, room.roomId)
            if progress is None:
                raise HTTPException(status_code=404, detail="challengeProgress 가 없습니다.")

            # 조건 필터링 (tag, status)
            if tag is not None and tag not in challenge.chTags:
                continue
            if status and room.status != status:
                continue
            
            summary = MyChallengeSummaryDto(
                roomId=room.roomId,
                title= challenge.title,
                progress=progress,
                participantsNum=room.participants,
                start=room.startDate,
                end=room.endDate
            )

            myChallengeSummaryLists.append(summary)

        return MyChallengeListResDto(
            memberName=member.memberId,
            tags=member.interest,
            myChallenges=myChallengeSummaryLists
        )