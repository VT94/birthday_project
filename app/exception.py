class BaseApiException(Exception):
    def __init__(self, message, status_code=None):
        super().__init__(message)

        if status_code is not None:
            self.status_code = status_code


class ServiceApiError(BaseApiException):
    status_code = 500

    def __init__(self, message, status_code=None, errors=None):
        super().__init__(message, status_code=status_code or self.status_code)
        self.message = message
        self.errors = errors


class BadRequestError(ServiceApiError):
    status_code = 400

    def __init__(self, message='Bad request', errors=None):
        super().__init__(message, errors=errors)
