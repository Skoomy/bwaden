import logging
from datetime import datetime
from typing import Any, Optional

import pandas as pd

from .base import DataProvider

logger = logging.getLogger(__name__)


class DataManager:
    """Manages data collection from multiple providers with failover support."""

    def __init__(
        self, primary_provider: DataProvider, backup_provider: Optional[DataProvider] = None
    ):
        """Set primary and backup data providers."""
        self.primary_provider = primary_provider
        self.backup_provider = backup_provider

    def get_historical_data(
        self,
        symbol: str,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
    ) -> pd.DataFrame:
        """Fetch historical data with failover support."""
        try:
            return self.primary_provider.fetch_historical_data(symbol, start_date, end_date)
        except Exception as e:
            logger.warning(
                f"Primary provider failed for {symbol}, trying backup provider: {str(e)}"
            )
            if self.backup_provider:
                return self.backup_provider.fetch_historical_data(symbol, start_date, end_date)
            raise

    def get_company_info(self, symbol: str) -> dict[str, Any]:
        """Fetch company information with failover support."""
        try:
            return self.primary_provider.fetch_company_info(symbol)
        except Exception as e:
            logger.warning(f"Primary provider failed for {symbol} info, trying backup: {str(e)}")
            if self.backup_provider:
                return self.backup_provider.fetch_company_info(symbol)
            raise
