from .connection.api import HonAPI
from .hon import Hon
import logging
_LOGGER = logging.getLogger(__name__)
_LOGGER.warning("Loaded pyhOn from NoUsername10's fork!")

__all__ = ["Hon", "HonAPI"]
