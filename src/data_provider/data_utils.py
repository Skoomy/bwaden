import logging

from src.data_provider.data_manager import DataManager
from src.data_provider.yahoo_provider import YahooFinanceProvider

logger = logging.getLogger(__name__)

# , AlphaVantageProvider


# Function to setup data manager
def setup_data_manager() -> DataManager:
    """Initialize the DataManager with providers."""
    # import os

    logger.info("Setting up data manager ...")
    try:
        # Initialize primary provider (Yahoo Finance)
        yf_provider = YahooFinanceProvider()

        # # Initialize backup provider (Alpha Vantage) if API key is available
        # av_key = os.getenv('ALPHA_VANTAGE_API_KEY')
        # av_provider = AlphaVantageProvider(api_key=av_key) if av_key else None

        return DataManager(
            primary_provider=yf_provider,
            # backup_provider=av_provider
        )
    except Exception as e:
        logger.error(f"Error setting up data manager: {str(e)}")
        raise ValueError("Error setting up data manager") from e
