from enum import Enum

# 나이대
class AgeGroupEnum(str, Enum):
    AGE_10s = "AGE_10s"
    AGE_20s = "AGE_20s"
    AGE_30s = "AGE_30s"
    AGE_40s = "AGE_40s"
    AGE_50s = "AGE_50s"
    AGE_60s = "AGE_60s"

    @classmethod
    def to_korean(cls, value):
        mapping = {
            cls.AGE_10s: "10대",
            cls.AGE_20s: "20대",
            cls.AGE_30s: "30대",
            cls.AGE_40s: "40대",
            cls.AGE_50s: "50대",
            cls.AGE_60s: "60대"
        }
        return mapping.get(value)

# 직업
class JobEnum(str, Enum):
    MIDDLE_SCHOOL = "MIDDLE_SCHOOL"
    HIGH_SCHOOL = "HIGH_SCHOOL"
    UNIVERSITY = "UNIVERSITY"
    EMPLOYEE = "EMPLOYEE"
    SELF_EMPLOYED = "SELF_EMPLOYED"
    UNEMPLOYED = "UNEMPLOYED"
    HOUSEWIFE = "HOUSEWIFE"
    JOB_SEEKER = "JOB_SEEKER"

    @classmethod
    def to_korean(cls, value):
        mapping = {
            cls.MIDDLE_SCHOOL: "중학생",
            cls.HIGH_SCHOOL: "고등학생",
            cls.UNIVERSITY: "대학생",
            cls.EMPLOYEE: "직장인",
            cls.SELF_EMPLOYED: "자영업자",
            cls.UNEMPLOYED: "무직",
            cls.HOUSEWIFE: "전업주부",
            cls.JOB_SEEKER: "취업준비생"
        }
        return mapping.get(value)

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
    CONSUMPTION = "소비"
    FINANCIAL_EDUCATION = "금융교육"
    INVESTMENT = "투자"

    @classmethod
    def to_korean(cls, code: str) -> str:
        try:
            return cls[code].value
        except KeyError:
            return code  # 매칭되는 enum이 없는 경우 원본값 반환