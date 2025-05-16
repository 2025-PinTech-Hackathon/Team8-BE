from fastapi import APIRouter
from src.main.router.MainAPIRouter import MainAPIRouter
from src.main.router.FeedAPIRouter import FeedAPIRouter
from src.main.router.ChallengeAPIRouter import ChallengeAPIRouter
from src.main.router.ProfileAPIRouter import ProfileAPIRouter

from src.main.health.router import HealthAPIRouter


router = APIRouter(
    prefix="",
)

router.include_router(HealthAPIRouter.router)
router.include_router(MainAPIRouter)
router.include_router(FeedAPIRouter)
router.include_router(ChallengeAPIRouter)
router.include_router(ProfileAPIRouter)