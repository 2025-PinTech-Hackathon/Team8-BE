from enum import Enum

class ChallengeStatusEnum(str, Enum):
    RECRUITING = "모집중"
    IN_PROGRESS = "진행중"
    COMPLETED = "진행완료"