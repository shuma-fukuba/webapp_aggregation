import requests
from fastapi import Depends, HTTPException
from starlette.status import HTTP_400_BAD_REQUEST
from .JWTBearer import JWKS, JWTBearer, JWTAuthorizationCredentials
from env import WEBAPP_AWS_COGNITO_REGION, WEBAPP_AWS_COGNITO_USER_POOL_ID

jwks = JWKS.parse_obj(
    requests.get(
        f'https://cognito-idp.{WEBAPP_AWS_COGNITO_REGION}.amazonaws.com/'
        f'{WEBAPP_AWS_COGNITO_USER_POOL_ID}/.well-known/jwks.json'
    ).json()
)

auth = JWTBearer(jwks)


async def get_current_user(credentials: JWTAuthorizationCredentials = Depends(auth)) -> str:
    try:
        return credentials.claims['cognito:username']
    except KeyError:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST,
                            detail='User attributes missing.')

async def get_current_username(credentials: JWTAuthorizationCredentials = Depends(auth)) -> str:
    try:
        return credentials.claims['sub']
    except KeyError:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST,
                            detail='User attributes missing.')
