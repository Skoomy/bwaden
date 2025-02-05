import logging
import sys
from datetime import datetime, timedelta
from typing import Optional, Union

import click

from src.cli_tool.display import display_company_info, display_stock_data
from src.data_provider.data_utils import setup_data_manager

# from rich.console import Console


logger = logging.getLogger(__name__)


@click.group()
def cli() -> None:
    """Stock Analysis Tool CLI."""
    pass


@click.command()
@click.option("--pipeline", default="data_collection", help="")
@click.option("--symbols", default="AAPL", help="Comma-separated list of stock symbols")
@click.option("--days", default=30, help="Number of days of historical data to fetch")
def runner(symbols: str, days: int, pipeline: str = "data_collection") -> None:
    """Run the specified pipeline."""
    click.clear()
    click.secho(f"Running pipeline: {pipeline}", fg="green")

    # if pipeline == 'data_collection':
    #     try:
    #         data_manager = setup_data_manager()
    #         symbol_list = [s.strip() for s in symbols.split(',')]
    #          # Calculate dates
    #         end_date = datetime.now()
    #         start_date = end_date - timedelta(days=days)
    #     except Exception as e:
    #         logger.error(f"Error: {str(e)}")
    #         click.secho(f"Error: {str(e)}", fg="red")
    #         sys.exit(1)

    #     return

    # except Exception as e:
    #       logger.error(f"Pipeline error: {str(e)}")
    #       click.secho(f"Pipeline error: {str(e)}", fg="red")
    #       sys.exit(1)


@cli.command()
@click.argument("symbol", help="Stock symbol to fetch data for")
@click.option(
    "--end_date",
    help="End date for historical data (format: YYYY-MM-DD)",
    # type=click.STRING,
)
@click.option(
    "--start_date",
    help="Start date for historical data (format: YYYY-MM-DD)",
    # type=click.STRING,
)
@click.option(
    "--days",
    default=30,
    help="Number of days of historical data to fetch (default: 30)",
    # type=click.INT,
)
def fetch(
    symbol: str,
    days: int,
    start_date: Optional[Union[str, datetime]] = None,
    end_date: Optional[Union[str, datetime]] = None,
) -> dict:
    """Fetch data for a single symbol."""
    # Convert start_date if it's a string
    if start_date is not None:
        if isinstance(start_date, str):
            start_date = datetime.strptime(start_date, "%Y-%m-%d")
        elif not isinstance(start_date, datetime):
            raise ValueError("start_date must be either a string (YYYY-MM-DD) or datetime object")

    # Convert end_date if it's a string
    if end_date is not None:
        if isinstance(end_date, str):
            end_date = datetime.strptime(end_date, "%Y-%m-%d")
        elif not isinstance(end_date, datetime):
            raise ValueError("end_date must be either a string (YYYY-MM-DD) or datetime object")

    # If days is provided, override start_date and end_date
    if days:
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days)
        data_manager = setup_data_manager()
    try:
        # Fetch and display data
        click.secho(f"Fetching data for {symbol}...", fg="yellow")
        historical_data = data_manager.get_historical_data(
            symbol=symbol, start_date=start_date, end_date=end_date
        )
        # print(historical_data)
        display_stock_data(historical_data, symbol)
        company_info = data_manager.get_company_info(symbol)
        display_company_info(company_info)

        # display_stock_data(historical_data, symbol)
        return {"strock_data": historical_data, "company_info": company_info}

    except Exception as e:
        logger.error(f"Error: {str(e)}")
        click.secho(f"Error: {str(e)}", fg="red")
        sys.exit(1)


if __name__ == "__main__":
    cli()
