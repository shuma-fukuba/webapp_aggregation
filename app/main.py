# ref: https://zenn.dev/yusugomori/articles/a3d5dc8baf9e386a58e5
from starlette.middleware.base import BaseHTTPMiddleware
from middlewares import http_log
from fastapi import FastAPI, APIRouter, Depends
from starlette.middleware.cors import CORSMiddleware
import env
from modules.auth import JWTBearer, jwks
from routers.private.home import router as home_router
from routers.open.curriculum import router as curriculum_router

router = APIRouter()
auth = JWTBearer(jwks)

private_router = APIRouter()
open_router = APIRouter()

private_router.include_router(home_router,
                              prefix='/home')

open_router.include_router(curriculum_router,
                           prefix='/curriculums')

router.include_router(private_router,
                      prefix='/private',
                      dependencies=[Depends(auth)])

router.include_router(open_router,
                      prefix='/open')

if env.APP_ENV == 'development':
    app = FastAPI()
else:
    app = FastAPI(docs_url=None,
                  redoc_url=None,
                  openapi_url=None)

app.include_router(
    router,
    prefix='/v1'
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

app.add_middleware(BaseHTTPMiddleware, dispatch=http_log)


@app.get('/')
def root():
    return {'Hello': 'World'}
