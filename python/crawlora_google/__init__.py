"""Typed Google client for the Crawlora hosted API."""

from .platform import GoogleClient, AsyncGoogleClient
from .client import CrawloraClientError, CrawloraError, CrawloraNetworkError, CrawloraServerError
from .operations import OPERATION_COUNT, OPERATION_IDS, PLATFORM

Client = GoogleClient
AsyncClient = AsyncGoogleClient
__version__ = '0.1.0'
DISPLAY_NAME = 'Google'
PLATFORM = 'google'
CONTRACT_REVISION = 'sha256:9cafd22a7c790c21e2881fc7de7512496dacd71de9bd3ef0f99f13cef7e4adc2'

__all__ = [
    "GoogleClient", "AsyncGoogleClient", "Client", "AsyncClient",
    "CrawloraError", "CrawloraClientError", "CrawloraServerError", "CrawloraNetworkError",
    "DISPLAY_NAME", "PLATFORM", "CONTRACT_REVISION", "OPERATION_COUNT", "OPERATION_IDS", "__version__",
]
