from fastapi import APIRouter
from src.main.router.MainAPIRouter import MainAPIRouter
from src.main.router import MyChallengeRouter
from src.main.router import MyChallengeListRouter

from src.main.health.router import HealthAPIRouter


router = APIRouter(
    prefix="",
)

router.include_router(HealthAPIRouter.router)
router.include_router(MainAPIRouter)
router.include_router(MyChallengeRouter.router)
router.include_router(MyChallengeListRouter.router)