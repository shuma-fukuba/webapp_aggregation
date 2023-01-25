from fastapi import APIRouter
from modules.http.Response import Response
from modules.laravel import curriculum as req

router = APIRouter()


@router.get('/')
async def read_learning_log():
    res = req.read_langs_contents()
    return Response(res)
