from fastapi import APIRouter, Depends
from modules.auth import get_current_username
from modules.http.Response import Response
from modules.laravel import home as req

router = APIRouter()


@router.get('/')
async def read_learning_log(user_id = Depends(get_current_username)):
    res = req.read_home(user_id=user_id)
    return Response(res)
