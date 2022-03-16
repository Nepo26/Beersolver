#!/bin/env python3

import click
from exercises.ThirdChapter import CliCommands

third_cli = CliCommands.exercise_three_c_6


@click.group()
def group():
    pass


if __name__ == '__main__':
    group.add_command(third_cli)

    group()
