import pandas as pd
from rich.console import Console
from rich.table import Table

console = Console()


def display_stock_data(data: pd.DataFrame, symbol: str) -> None:
    """Display stock data in a formatted table."""
    table = Table(title=f"Stock Data for {symbol}")

    # Add columns
    table.add_column("Date", justify="left", style="cyan")
    table.add_column("Open", justify="right")
    table.add_column("High", justify="right")
    table.add_column("Low", justify="right")
    table.add_column("Close", justify="right")
    table.add_column("Volume", justify="right")

    # Add rows
    for index, row in data.iterrows():
        table.add_row(
            str(index.date()),
            f"{row['open']:.2f}",
            f"{row['high']:.2f}",
            f"{row['low']:.2f}",
            f"{row['close']:.2f}",
            f"{row['volume']:,}",
        )

    console.print(table)


def display_company_info(company_info: dict) -> None:
    """Display company information in a formatted table."""
    console.print("\n[bold]Company Information:[/bold]")
    try:
        for key, value in company_info.items():
            if value is not None:
                console.print(f"{key.replace('_', ' ').title()}: {value}")
    except Exception as e:
        console.print(f"Error displaying company information: {str(e)}")
        raise
