__all__ = [
    "UserAlreadyExistError",
    "UserDoesNotExistError",
    "UnsupportedUserModelError",
    "PermissionDeniedError",
    "DataMalformedOrNotProvidedError",
]

from .api import DataMalformedOrNotProvidedError
from .web import (
    PermissionDeniedError,
    UnsupportedUserModelError,
    UserAlreadyExistError,
    UserDoesNotExistError,
)
