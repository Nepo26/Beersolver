#!/bin/env python3

import click

from exercises.ThirdChapter.commands import exercise_three_c_6
from utils.log import InternalLogger


@click.group()
@click.option("--debug", is_flag=True, help="Start debugging mode")
@click.pass_context
def cli(ctx, debug):
    if debug:
        print("Debugging mode is ON")
        logger = InternalLogger(debug)
    else:
        logger = InternalLogger()

    ctx.obj = logger


if __name__ == '__main__':
    cli.add_command(exercise_three_c_6)

    cli()
