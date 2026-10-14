"""Typed Google client for the Crawlora hosted API."""

from .platform import GoogleClient, AsyncGoogleClient
from .client import CrawloraClientError, CrawloraError, CrawloraNetworkError, CrawloraServerError
from .operations import OPERATION_COUNT, OPERATION_IDS, PLATFORM

Client = GoogleClient
AsyncClient = AsyncGoogleClient
__version__ = '0.2.0'
DISPLAY_NAME = 'Google'
PLATFORM = 'google'
CONTRACT_REVISION = 'sha256:8db88e8b908a130295c5df80bead8c65485e1eb4a293ceaa55add4ec77d7d071'

__all__ = [
    "GoogleClient", "AsyncGoogleClient", "Client", "AsyncClient",
    "CrawloraError", "CrawloraClientError", "CrawloraServerError", "CrawloraNetworkError",
    "DISPLAY_NAME", "PLATFORM", "CONTRACT_REVISION", "OPERATION_COUNT", "OPERATION_IDS", "__version__",
]
