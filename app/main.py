# ref: https://zenn.dev/yusugomori/articles/a3d5dc8baf9e386a58e5
from starlette.middleware.base import BaseHTTPMiddleware
from middlewares import http_log
from fastapi import FastAPI, APIRouter, Depends
from starlette.middleware.cors import CORSMiddleware
import env
from modules.auth import JWTBearer, jwks
from routers.home import router as home_router

router = APIRouter()
auth = JWTBearer(jwks)

router.include_router(home_router,
                      prefix='/home',
                      tags=['home'])

if env.APP_ENV == 'development':
    app = FastAPI()
else:
    app = FastAPI(docs_url=None,
                  redoc_url=None,
                  openapi_url=None)

app.include_router(
    router,
    prefix='/v1',
    dependencies=[Depends(auth)]
)

origins = [
    env.WEBAPP_REACT_HOST,
    f'https://{env.WEBAPP_REACT_HOST}'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.get('/')
def root():
    return {'Hello': 'World'}


app.add_middleware(BaseHTTPMiddleware, dispatch=http_log)
