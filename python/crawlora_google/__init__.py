"""Typed Google client for the Crawlora hosted API."""

from .platform import GoogleClient, AsyncGoogleClient
from .client import CrawloraClientError, CrawloraError, CrawloraNetworkError, CrawloraServerError
from .operations import OPERATION_COUNT, OPERATION_IDS, PLATFORM

Client = GoogleClient
AsyncClient = AsyncGoogleClient
__version__ = '0.2.1'
DISPLAY_NAME = 'Google'
PLATFORM = 'google'
CONTRACT_REVISION = 'sha256:a04744a8cf0d1b2f64f4a5508b782d97fdc88a38edbd067a3c0d8fe5e8c401df'

__all__ = [
    "GoogleClient", "AsyncGoogleClient", "Client", "AsyncClient",
    "CrawloraError", "CrawloraClientError", "CrawloraServerError", "CrawloraNetworkError",
    "DISPLAY_NAME", "PLATFORM", "CONTRACT_REVISION", "OPERATION_COUNT", "OPERATION_IDS", "__version__",
]
