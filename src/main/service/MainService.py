from src.main.repository.MainRepository import MainRepository
from src.main.domain.dto.InformationResponseDto import UserInformationResponse, Feed
from sqlalchemy.orm import Session
from src.main.domain.dto.ChallengeResponseDto import UserChallengeResponse, ChallengeResponseDto
from src.main.domain.model.MemberEnum import InterestEnum
from sqlalchemy import func
from src.main.domain.model.Information import Information
from src.main.domain.model.Challenge import Challenge

class MainService:
    def __init__(self, db: Session):
        self.repository = MainRepository(db)
    
    def get_information_by_tag(self, member_id: str, tag: str | None) -> UserInformationResponse | None:
        member = self.repository.get_member_by_id(member_id)
        if not member:
            return None

        user_interests = member.interest  # ex: ["INVESTMENT", "SCHOLOARSHIP"]

        # tag가 None이거나 "null"이라는 문자열로 들어올 경우 전체 관심사로 조회
        if tag is None or tag.lower() == "null":
            infos = self.repository.get_information_by_multiple_tags(user_interests)
        else:
            # tag가 유효한 Enum인지 확인하고, Enum value(한글)로 변환
            try:
                tag_value = InterestEnum[tag].value  # ex: "투자"
            except KeyError:
                return None

            # 사용자의 관심사에 해당하는 tag인지 확인
            if tag not in user_interests:
                return None

            infos = self.repository.get_information_by_tag(tag_value)

        # Feed 생성 (tag가 None일 경우 info.tags[0] 사용)
        feeds = []
        for info in infos:
            used_tag = tag_value if tag and tag.lower() != "null" else (info.tags[0] if info.tags else "기타")

            feeds.append(
                Feed(
                    informationId=info.informationId,
                    title=info.title,
                    content=info.content,
                    tag=used_tag
                )
            )

        # Enum key → value로 변환해서 categories 출력 (예: "INVESTMENT" → "투자")
        categories = [
            InterestEnum[item].value if item in InterestEnum.__members__ else item
            for item in user_interests
        ]

        return UserInformationResponse(
            memberId=member.memberId,
            userName=member.name,
            categories=categories,
            feeds=feeds
        )
    
    def get_information_by_specific_tag(self, member_id: str, tag: str) -> UserInformationResponse | None:
        member = self.repository.get_member_by_id(member_id)
        if not member:
            return None

        user_interests = member.interest

        # 여기서 tag_value로 변환하지 말고, tag 그대로 사용 (예: "SCHOLOARSHIP")
        if tag not in user_interests:
            return None

        # DB의 tags가 ["SCHOLOARSHIP"]처럼 저장되어 있으므로, tag 그대로 사용
        infos = self.repository.db.query(Information).filter(
            func.json_search(Information.tags, 'one', tag) != None
        ).all()

        feeds = [
            Feed(
                informationId=info.informationId,
                title=info.title,
                content=info.content,
                tag=tag  # 그대로 넣기
            ) for info in infos
        ]

        # 사용자 관심사 키 값 → 한글로 변환
        categories = [
            InterestEnum[item].value if item in InterestEnum.__members__ else item
            for item in user_interests
        ]

        return UserInformationResponse(
            memberId=member.memberId,
            userName=member.name,
            categories=categories,
            feeds=feeds
        )
    
    def get_challenge_by_specific_tag(self, member_id: str, tag: str) -> UserChallengeResponse | None:
        member = self.repository.get_member_by_id(member_id)
        if not member:
            return None

        user_interests = member.interest
        if tag not in user_interests:
            return None

        # DB의 ch_tags는 ["SCHOLOARSHIP"] 형태로 저장되어 있으므로 변환 없이 그대로 사용
        challenges = self.repository.db.query(Challenge).filter(
            func.json_search(Challenge.chTags, 'one', tag) != None
        ).all()

        return UserChallengeResponse(
            userName=member.name,
            categories=[
                InterestEnum[item].value if item in InterestEnum.__members__ else item
                for item in user_interests
            ],
            challenges=[
                ChallengeResponseDto(
                    challengeId=challenge.challengeId,
                    title=challenge.title,
                    description=challenge.content,
                    tag=tag
                ) for challenge in challenges
            ]
        )
    
    def get_challenge_by_all_tags(self, member_id: str) -> UserChallengeResponse | None:
        member = self.repository.get_member_by_id(member_id)
        if not member:
            return None

        user_interests = member.interest
        tag_keys = [tag for tag in user_interests if tag in InterestEnum.__members__]
        tag_values = tag_keys  # 그대로 Enum 키로 검색 (ex: "TRAVEL")

        challenges = self.repository.get_challenges_by_tag(tag_values)

        return UserChallengeResponse(
            userName=member.name,
            categories=[
                InterestEnum[item].value if item in InterestEnum.__members__ else item
                for item in user_interests
            ],
            challenges=[
                ChallengeResponseDto(
                    challengeId=challenge.challengeId,
                    title=challenge.title,
                    description=challenge.content,
                    tag=challenge.chTags[0] if challenge.chTags else "기타"
                ) for challenge in challenges
            ]
        )


    def get_tags(self) -> list[str]:
        return self.repository.get_tags()