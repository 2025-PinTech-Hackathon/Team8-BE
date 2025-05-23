from ast import List
from datetime import date, timedelta
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
import random
import traceback
import sys

from src.main.repository.MemberChallengeRoomRepository import MemberChallengeRoomRepository
from src.main.domain.model.ChallengeRoom import ChallengeRoom
from src.main.domain.model.CodeTable import CodeTable
from src.main.domain.model._MemberChallengeRoom import MemberChallengeRoom
from src.main.domain.model.CheckTable import CheckTable
from src.main.domain.dto.MyChallengeDto import MyChallengeReqDto
from src.main.domain.dto.MyChallengeDto import MyChallengeRoomResDto
from src.main.repository.ChallengeRoomRepository import ChallengeRoomRepository
from src.main.domain.model.Challenge import Challenge
from src.main.repository.ChallengeRepository import ChallengeRepository
from src.main.repository.CheckRepository import CheckRepository
from src.main.repository.MemberRepository import MemberRepository
from src.main.domain.dto.MyChallengeDto import Friend
from src.main.domain.dto.MyChallengeDto import FriendsProgress
from src.main.domain.dto.MyChallengeDto import Day
from src.main.domain.dto.MyChallengeDto import Days
from src.main.domain.dto.MyChallengeDto import InviteCodeResponseDto, ParticipateResponseDto
from src.main.domain.model.ChallengeStatusEnum import ChallengeStatusEnum


class MyChallengeService:
    @staticmethod
    def create_room(session: AsyncSession, memberId:str, challengeId: int):
        #이미 있는지부터 확인하기
        member_challenge_room = MemberChallengeRoomRepository.get_by_member_id_and_challenge_id(session, memberId, challengeId)

        if len(member_challenge_room) != 0:
            raise   HTTPException(status_code=400, detail="이미 하고 있는 챌린지방입니다.")
        
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

    @staticmethod
    def getFriendProgress(session:AsyncSession, memberId: str, roomId: int):
        #Check로 가서 roomId이면서 memberId가 아난 애들의 memberId를 List로 받아오기
        friend_ids_table: List[CheckTable] = CheckRepository.get_friend_ids(session, memberId, roomId)
        
        friendLists : List[Friend] = []

        #progress를 각각 구해야함
        for ids in friend_ids_table:
            friend = MemberRepository.get_by_member_id(session, ids.memberId)

            friend_progress=CheckRepository.get_progress(session, ids.memberId, roomId)
        
            friendDetail = Friend(
                friendId=friend.memberId,
                friendName=friend.name,
                progress=friend_progress,
            )

            friendLists.append(friendDetail)

        return FriendsProgress(
            friends=friendLists
            )
    
    @staticmethod
    def get_invite_code(session: AsyncSession, room_id: int) -> InviteCodeResponseDto:
        try:
            room: ChallengeRoom = ChallengeRoomRepository.get_by_id(session, room_id)
            if not room:
                raise HTTPException(status_code=404, detail="해당 챌린지 방이 존재하지 않습니다.")

            existing_code = ChallengeRoomRepository.get_invite_code_by_room_id(session, room_id)

            if existing_code:
                return InviteCodeResponseDto(invitedCode=existing_code.code)

            new_code = ''.join([str(random.randint(0, 9)) for _ in range(6)])

            ChallengeRoomRepository.create_or_update_invite_code(session, room_id, new_code)

            if room.status == ChallengeStatusEnum.IN_PROGRESS:
                room.status = ChallengeStatusEnum.RECRUITING
                session.add(room)

            session.commit()

            return InviteCodeResponseDto(invitedCode=new_code)

        except Exception:
            traceback.print_exc()
            raise HTTPException(status_code=500, detail="초대 코드를 불러오지 못했습니다.")
    
    @staticmethod
    def getFriendCalendar(session: AsyncSession, member_id: str, room_id: int):
        #check
        checkTable:List[CheckTable] = CheckRepository.get_by_id(session, member_id, room_id)

        dayList : List[Day] = []

        for check in checkTable:
            dayDetail = Day(
                date=check.date,
                isDone=check.done
            )

            dayList.append(dayDetail)

        return Days(
            days=dayList)

    @staticmethod
    def participate_in_challenge(session, code: str, member_id: str) -> ParticipateResponseDto:
        code_entry = session.execute(
            select(CodeTable).where(CodeTable.code == code)
        ).scalar_one_or_none()

        if not code_entry:
            raise HTTPException(status_code=404, detail="유효하지 않은 초대 코드입니다.")

        room_id = code_entry.roomId

        existing = session.execute(
            select(MemberChallengeRoom).where(
                (MemberChallengeRoom.memberId == member_id) &
                (MemberChallengeRoom.roomId == room_id)
            )
        ).scalar_one_or_none()

        if existing:
            return ParticipateResponseDto(roomId=room_id, status="이미 참여한 챌린지입니다.")

        new_entry = MemberChallengeRoom(memberId=member_id, roomId=room_id)
        session.add(new_entry)

        room: ChallengeRoom = session.execute(
            select(ChallengeRoom).where(ChallengeRoom.roomId == room_id)
        ).scalar_one()

        if room.participants is None:
            room.participants = 1
        else:
            room.participants += 1

        # 인원이 5명이 되면 상태를 IN_PROGRESS로 변경
        if room.participants >= 5 and room.status == ChallengeStatusEnum.RECRUITING:
            room.status = ChallengeStatusEnum.IN_PROGRESS

        session.add(room)
        session.commit()

        return ParticipateResponseDto(roomId=room_id, status="참여 완료")
