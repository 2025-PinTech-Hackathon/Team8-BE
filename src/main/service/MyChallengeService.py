from datetime import date, timedelta
from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException

from src.main.repository.MemberChallengeRoomRepository import MemberChallengeRoomRepository
from src.main.domain.model.ChallengeRoom import ChallengeRoom
from src.main.domain.model.MemberChallengeRoom import member_challenge_room
from src.main.domain.model.CheckTable import CheckTable

class MyChallengeService:
    @staticmethod
    async def create_room(session: AsyncSession, memberId:str, challengeId: int):
        #이미 있는지부터 확인하기
        member_challenge_room = await MemberChallengeRoomRepository.get_by_member_id(session, memberId)

        if member_challenge_room:
            raise HTTPException(status_code=400, detail="이미 하고 있는 챌린지방입니다.")
        
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
        await session.flush() 

        new_checkTable = CheckTable(
            date=None,
            done=None,
            memberId=memberId,
            roomId=new_room.roomId
        )
        
    
        session.add(new_checkTable)

        # 3. member_challenge_room 관계 등록
        await session.execute(
            insert(member_challenge_room).values(
                member_id=memberId,
                room_id=new_room.roomId
            )
        )

        await session.commit()

        return new_room.roomId

