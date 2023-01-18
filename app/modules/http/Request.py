# Ref:
#   http://fakatatuku.hatenablog.com/entry/2015/03/26/233024

import requests
from requests.exceptions import Timeout
from .error import TimeoutException


class Request:
    HEADERS = {'content-type': 'application/json'}
    TIMEOUT = 120
    _PREFIX = None

    @classmethod
    def prefix(cls) -> str:
        if cls._PREFIX is None:
            raise NotImplementedError('_PREFIX must be specified.')
        return cls._PREFIX

    @classmethod
    def get(cls, url: str, **kwargs):
        try:
            res = requests.get(f'{cls.prefix()}/{url}',
                               headers=cls.HEADERS,
                               timeout=cls.TIMEOUT, **kwargs)
        except Timeout:
            res = TimeoutException()

        return res

    # @classmethod
    # def get_file(cls, url: str, **kwargs):
    #     try:
    #         res = requests.get(f'{cls.prefix()}/{url}',
    #                            timeout=cls.TIMEOUT, **kwargs)
    #     except Timeout:
    #         res = TimeoutException()

    #     return res

    @classmethod
    def post(cls, url: str, **kwargs):
        try:
            res = requests.post(f'{cls.prefix()}/{url}',
                                headers=cls.HEADERS,
                                timeout=cls.TIMEOUT, **kwargs)
        except Timeout:
            res = TimeoutException()

        return res

    @classmethod
    def put(cls, url: str, **kwargs):
        try:
            res = requests.put(f'{cls.prefix()}/{url}',
                               headers=cls.HEADERS,
                               timeout=cls.TIMEOUT, **kwargs)
        except Timeout:
            res = TimeoutException()

        return res

    @classmethod
    def delete(cls, url: str, **kwargs):
        try:
            res = requests.delete(f'{cls.prefix()}/{url}',
                                  headers=cls.HEADERS,
                                  timeout=cls.TIMEOUT, **kwargs)

        except Timeout:
            res = TimeoutException()

        return res
