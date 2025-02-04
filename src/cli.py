import logging

import click

# import pandas as pd


logger = logging.getLogger(__name__)


@click.command()
@click.option("--pipeline", default="data_collection", help="")
def runner(pipeline: str = "data_collection"):
    """ """
    click.clear()

    click.secho(f"Running pipeline: {pipeline}", fg="green")

    if pipeline == pipeline:
        return
