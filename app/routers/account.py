from fastapi import APIRouter


account_router = APIRouter(prefix="/account")


@account_router.get("/myself")
def get_my_account():
    pass


@account_router.patch("/myself")
def update_my_account():
    pass


@account_router.get("/{user_id}")
def get_user_account():
    pass
