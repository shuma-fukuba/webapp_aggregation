from starlette.status import HTTP_408_REQUEST_TIMEOUT


class ResponseException:
    def __init__(self, status_code: int, text: str) -> None:
        self._status_code = status_code
        self._text = text

    @property
    def status_code(self):
        return self._status_code

    @property
    def text(self):
        return self._text


class TimeoutException(ResponseException):
    def __init__(self):
        status_code = HTTP_408_REQUEST_TIMEOUT
        text = 'Connection timed out.'

        super().__init__(status_code, text)
