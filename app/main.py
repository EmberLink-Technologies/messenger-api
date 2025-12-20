from fastapi import FastAPI

from .routers.account import account_router
from .routers.auth import auth_router


app = FastAPI()


app.include_router(account_router)
app.include_router(auth_router)
