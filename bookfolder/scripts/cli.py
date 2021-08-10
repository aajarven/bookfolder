"""
Command line interface for the bookfolder app.
"""

import click

from bookfolder.formatter import CSVFormatter
from bookfolder.pattern_creator import PatternCreator


@click.group()
@click.argument("image", type=click.Path(exists=True))
@click.pass_context
def cli(ctx, image):
    """
    Generate a bookfolding pattern from IMAGE

    Each color of pixels in the image must correspond to one fold depth in the
    scuplture, with each horizontal pixel corresponding to one sheet of paper
    in the book and each vertical pixel to one MEASUREMENT_INTERVAL along the
    edge of the book.
    """
    ctx.ensure_object(dict)
    ctx.obj["image"] = image


@cli.command()
@click.pass_context
@click.option("--measurement-interval",
              help="Height of one pixel in the IMAGE in millimeters",
              default=0.25)
def csv_pattern(ctx, measurement_interval):
    """
    Generate the pattern from the given IMAGE and print it in csv format.
    """
    image = ctx.obj["image"]
    pattern_creator = PatternCreator(image, measurement_interval)
    sheets = pattern_creator.sheets()
    formatter = CSVFormatter(sheets)
    click.echo(formatter.format())


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    # pylint: disable=unexpected-keyword-arg
    cli(obj={})
