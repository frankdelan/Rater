from starlette.middleware.cors import CORSMiddleware

from api.position import position_router
from api.property import property_router
from api.rating import rating_router
from api.user import user_router

from settings.swagger import create_app

app = create_app(
    custom_static_url=True
)

app.include_router(user_router)
app.include_router(rating_router)
app.include_router(property_router)
app.include_router(position_router)

origins = [
    'http://localhost:8000',

]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
