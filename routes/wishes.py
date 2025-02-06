from fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from sqlmodel import select
from models import User, Wish
from db import SessionDeep


route = APIRouter()

@route.post('/wish/{user_id}')
def create_wish(user_id:str, wishes: list[Wish], session: SessionDeep):
    print(f' whishes { wishes } id {user_id} - {type(user_id)} { int(user_id)}')
    user = session.get(User, int(user_id))
    print(f'{user}')
    if not user:
        raise HTTPException(status_code=404, detail="User not found....")
    for wish in wishes:
        wish.user_id = user.id
        session.add(wish)
        session.commit()
        session.refresh(wish)
        
        
    return JSONResponse(content={'message': 'Lista Agregada'})  



@route.get('/wish/{user_id}')
def create_wish(user_id:str, session: SessionDeep):	
    wishes = session.exec(select(Wish).where(Wish.user_id == int(user_id))).all()
    print(f'wishes {wishes}')
    return {"wishes": [wish.model_dump() for wish in wishes]}
      