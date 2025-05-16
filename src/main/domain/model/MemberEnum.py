from enum import Enum

# 나이대
class AgeGroupEnum(str, Enum):
    AGE_10s = "10대"
    AGE_20s = "20대"
    AGE_30s = "30대"
    AGE_40s = "40대"
    AGE_50s = "50대"
    AGE_60s = "60대 이상"

# 직업
class JobEnum(str, Enum):
    MIDDLE_SCHOOL = "중학생"
    HIGH_SCHOOL = "고등학생"
    UNIVERSITY = "대학생"
    EMPLOYEE = "직장인"
    SELF_EMPLOYED = "자영업"
    UNEMPLOYED = "무직"
    HOUSEWIFE = "주부"
    JOB_SEEKER = "취업준비생"

# 관심사 (카테고리)
class InterestEnum(str, Enum):
    SCHOLOARSHIP = "장학금"
    HOUSING_SUPPORT = "주거지원"
    YOUTH_HOUSING = "청년주거"
    NEWLYWED = "신혼부부"
    TRAVEL = "여행"
    TAX = "세금"
    EMPLOYMENT = "취업지원"
    INSURANCE = "보험"
    RETIREMENT = "노후"
    SALE_INFO = "분양정보"