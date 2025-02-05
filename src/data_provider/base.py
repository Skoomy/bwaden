import logging
from abc import ABC, abstractmethod
from datetime import datetime
from typing import Any, Dict, Optional

# from alpha_vantage.timeseries import TimeSeries
import pandas as pd

logger = logging.getLogger(__name__)


class DataProvider(ABC):
    """Abstract base class for data providers."""

    @abstractmethod
    def fetch_historical_data(
        self,
        symbol: str,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
    ) -> pd.DataFrame:
        """Fetch historical price data."""
        pass

    @abstractmethod
    def fetch_company_info(self, symbol: str) -> Dict[str, Any]:
        """Fetch company information."""
        pass
