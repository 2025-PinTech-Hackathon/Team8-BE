from datetime import date, timedelta
from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException

from src.main.repository.MemberChallengeRoomRepository import MemberChallengeRoomRepository
from src.main.domain.model.ChallengeRoom import ChallengeRoom
from src.main.domain.model._MemberChallengeRoom import MemberChallengeRoom
from src.main.domain.model.CheckTable import CheckTable
from src.main.domain.dto.MyChallengeDto import MyChallengeReqDto
from src.main.domain.dto.MyChallengeDto import MyChallengeRoomResDto
from src.main.repository.ChallengeRoomRepository import ChallengeRoomRepository
from src.main.domain.model.Challenge import Challenge
from src.main.repository.ChallengeRepository import ChallengeRepository
from src.main.repository.CheckRepository import CheckRepository


class MyChallengeService:
    @staticmethod
    def create_room(session: AsyncSession, memberId:str, challengeId: int):
        #이미 있는지부터 확인하기
        member_challenge_room = MemberChallengeRoomRepository.get_by_member_id_and_challenge_id(session, memberId, challengeId)

        if len(member_challenge_room) != 0:
            raise HTTPException(status_code=400, detail="이미 하고 있는 챌린지방입니다.")
        
        print("비어있는거 잘 작동")
        
        start = date.today()
        end = start + timedelta(days=7)

        #challengeRoom부터 만들기
        new_room = ChallengeRoom(
            challengeId = challengeId,
            status="진행중",
            startDate=start,
            endDate=end,
            participants=1
        )

        session.add(new_room)
        print(new_room.roomId)
        session.flush() 

        new_checkTable = CheckTable(
            date=None,
            done=None,
            memberId=memberId,
            roomId=new_room.roomId
        )
        
    
        session.add(new_checkTable)

        # 3. member_challenge_room 관계 등록
        new_memberChallengeRoom = MemberChallengeRoom(
            memberId = memberId,
            roomId=new_room.roomId
        )
        session.add(new_memberChallengeRoom)
        session.commit()
        
        mychallengereq = MyChallengeReqDto(
            roomId=new_room.roomId
        )

        return mychallengereq
    
    @staticmethod
    def getChallengeDetail(session: AsyncSession, memberId: str, roomId: int):
        #challengeRoom을 받기
        challengeRoom : ChallengeRoom = ChallengeRoomRepository.get_by_id(session, roomId)

        #challenge 받기
        challenge: Challenge = ChallengeRepository.get_by_challenge_id(session, challengeRoom.challengeId)
        
        #progress
        progress = CheckRepository.get_progress(session, memberId, roomId)

        myDetail = MyChallengeRoomResDto(
            title=challenge.title,
            status=challengeRoom.status,
            content=challenge.content,
            start=challengeRoom.startDate,
            end=challengeRoom.endDate,
            progress=progress,
        )

        return myDetail


