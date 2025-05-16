import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.main.service.MainService import MainService
from src.main.domain.model.Member import Member
from src.main.domain.model.Information import Information
from src.main.domain.database import Base
from uuid import uuid4


# 테스트용 SQLite 메모리 DB
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture
def db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()

    # 테스트 데이터 삽입
    test_member = Member(
        memberId="test123",
        name="홍길동",
        email="test@example.com",
        gender=True,
        age="AGE_20s",
        job="UNIVERSITY",
        interest=["장학금", "여행"]
    )
    test_info = Information(
        informationId=uuid4().hex,
        title="장학금 안내",
        content="누구나 신청 가능",
        tags=["장학금"]
    )

    db.add(test_member)
    db.add(test_info)
    db.commit()
    yield db
    db.close()


def test_get_information_by_tag_success(db):
    service = MainService(db)
    result = service.get_information_by_tag("test123", "장학금")
    
    assert result is not None
    assert result.memberId == "test123"
    assert result.userName == "홍길동"
    assert result.categories == ["장학금", "여행"]
    assert len(result.feeds) == 1
    assert result.feeds[0].title == "장학금 안내"


def test_get_information_by_category_no_user(db):
    service = MainService(db)
    result = service.get_information_by_tag("unknown_id", "장학금")
    assert result is None


def test_get_information_by_category_not_in_interest(db):
    service = MainService(db)
    result = service.get_information_by_tag("test123", "세금")
    assert result is None
