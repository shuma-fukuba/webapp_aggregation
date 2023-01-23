from fastapi import APIRouter, Depends
from modules.auth import get_current_username
from modules.http.Response import Response
from modules.laravel import home as req

router = APIRouter()


@router.get('/')
async def read_learning_log(user_id=Depends(get_current_username)):
    res = req.read_learning_log(user_id=user_id)
    return Response(res)


@router.post('/')
async def create_learning_log(params: dict, user_id=Depends(get_current_username)):
    res = req.create_learning_log(user_id=user_id, params=params)
    return Response(res)
