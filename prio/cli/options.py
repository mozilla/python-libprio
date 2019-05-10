import click
from .types import BYTE_STRING


def apply_options(func, options):
    for option in options:
        func = option(func)
    return func


def public_key(func):
    options = [
        click.option(
            "--public-key-internal",
            required=True,
            type=BYTE_STRING,
            help="The public key of the processing server.",
        ),
        click.option(
            "--public-key-external",
            required=True,
            type=BYTE_STRING,
            help="The public key of the co-processing server.",
        ),
    ]
    return apply_options(func, options)


def server_config(func):
    options = [
        click.option(
            "--server-id",
            required=True,
            type=click.Choice(["A", "B"]),
            help="The identifier for match.",
        ),
        click.option(
            "--private-key",
            required=True,
            type=BYTE_STRING,
            help="The private key of the processing server.",
        ),
        click.option(
            "--shared-secret",
            required=True,
            type=BYTE_STRING,
            help="The shared server secret encoded in base64.",
        ),
    ]
    return apply_options(func, options)


def output_1(func):
    options = [
        click.option(
            "--output",
            required=True,
            type=click.Path(file_okay=False),
            help="The path to the output directory.",
        )
    ]
    return apply_options(func, options)


def output_2(func):
    options = [
        click.option(
            "--output-A",
            required=True,
            type=click.Path(file_okay=False),
            help="The path to the input directory of server A.",
        ),
        click.option(
            "--output-B",
            required=True,
            type=click.Path(file_okay=False),
            help="The path to the input directory of server B.",
        ),
    ]
    return apply_options(func, options)


def input_1(func):
    options = [
        click.option(
            "--input",
            required=True,
            type=click.Path(dir_okay=False),
            help="File containing shares from clients.",
        )
    ]
    return apply_options(func, options)


def input_2(func):
    options = [
        click.option(
            "--input-internal",
            required=True,
            type=click.Path(dir_okay=False),
            help="File containing data generated by the processing server.",
        ),
        click.option(
            "--input-external",
            required=True,
            type=click.Path(dir_okay=False),
            help="File containing data generated by the co-processing server.",
        ),
    ]
    return apply_options(func, options)


def data_config(func):
    options = [
        click.option(
            "--batch-id",
            required=True,
            type=BYTE_STRING,
            help="A shared batch identifier used as a validity check.",
        ),
        click.option(
            "--n-data",
            required=True,
            type=click.INT,
            help="The size of the input bit-vector.",
        ),
    ]
    return apply_options(func, options)
