from modules.http import Request
from env import LARAVEL_API_HOST


class LaravelRequest(Request):
    _PREFIX = f'{LARAVEL_API_HOST}/v1'
