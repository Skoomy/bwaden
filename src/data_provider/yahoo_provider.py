# src/data_provider/yahoo_provider.py
import logging
from datetime import datetime, timedelta
from typing import Any, Dict, Optional

import pandas as pd
import yfinance as yf
from tenacity import retry, stop_after_attempt, wait_exponential

from src.data_provider.base import DataProvider

logger = logging.getLogger(__name__)


class YahooFinanceProvider(DataProvider):
    """Yahoo Finance data provider implementation."""

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
    def fetch_historical_data(
        self,
        symbol: str,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
    ) -> pd.DataFrame:
        """
        Fetch historical data from Yahoo Finance.

        Args:
            symbol: Stock ticker symbol
            start_date: Start date for historical data
            end_date: End date for historical data

        Returns:
            DataFrame with columns [Open, High, Low, Close, Volume, Dividends, Stock Splits]
        """
        try:
            # Default to 1 year of data if no dates specified
            if not start_date:
                start_date = datetime.now() - timedelta(days=365)
            if not end_date:
                end_date = datetime.now()

            ticker = yf.Ticker(symbol)
            df = ticker.history(start=start_date, end=end_date)

            if df.empty:
                raise ValueError(f"No data returned for symbol {symbol}")

            # Ensure consistent column naming
            df = df.rename(
                columns={
                    "Open": "open",
                    "High": "high",
                    "Low": "low",
                    "Close": "close",
                    "Volume": "volume",
                }
            )

            return df

        except Exception as e:
            logger.error(f"Error fetching data from Yahoo Finance for {symbol}: {str(e)}")
            raise

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
    def fetch_company_info(self, symbol: str) -> Dict[str, Any]:
        """Fetch company information from Yahoo Finance."""
        try:
            ticker = yf.Ticker(symbol)
            info = ticker.info

            # Extract relevant information
            return {
                "name": info.get("longName"),
                "sector": info.get("sector"),
                "industry": info.get("industry"),
                "market_cap": info.get("marketCap"),
                "pe_ratio": info.get("forwardPE"),
                "dividend_yield": info.get("dividendYield"),
                "beta": info.get("beta"),
                "description": info.get("longBusinessSummary"),
            }

        except Exception as e:
            logger.error(f"Error fetching company info for {symbol}: {str(e)}")
            raise
