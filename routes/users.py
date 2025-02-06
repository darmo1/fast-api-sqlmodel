from fastapi import APIRouter
from fastapi.responses import JSONResponse
from sqlmodel import select
from db import SessionDeep
from exceptions import UserAlreadyExistException
from models import User

route = APIRouter()

@route.post("/create-user", response_model=User, tags=["users"])
async def create_user(user: User, session: SessionDeep):
    # Validar que no exista
    existing_user = session.exec(select(User).where((User.email == user.email))).first()
    if not existing_user:
        new_user = session.add(user)
        print(f"El nuevo usuario es {new_user} y este {user}")
        session.commit()
        session.refresh(user)
        return user
    else:
        return existing_user

    # raise UserAlreadyExistException()

@route.post("/get-user", tags=["users"])
async def get_user(user:User, session: SessionDeep):
    print('Entré a get-user')
    existing_user = session.exec(select(User).where(User.email == user.email)).first()
    print(f'existing_user: {existing_user}')
    if existing_user:
        return JSONResponse(content={"error": False, "user": existing_user.model_dump()})
    else:
        return JSONResponse(content={"error": True, "user": None})
