from repositories.position import PositionRepository
from repositories.rating import RatingRepository
from repositories.user import UserRepository
from repositories.property import PropertyRepository

from services.position import PositionService
from services.rating import RatingService
from services.user import UserService
from services.property import PropertyService


def position_service():
    return PositionService(PositionRepository)


def rating_service():
    return RatingService(RatingRepository)


def user_service():
    return UserService(UserRepository)


def property_service():
    return PropertyService(PropertyRepository)
