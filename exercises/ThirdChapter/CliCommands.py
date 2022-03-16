import click
from numpy import array
from . import ThreeCSix as ModuleThreeCSix

ThreeCSix = ModuleThreeCSix.ThreeCSix


@click.command()
@click.option('--position_a', '--pos-a', nargs=3, type=float, prompt=True, prompt_required=False,
              help='Position A in format x y z')
@click.option('--position_e', '--pos-e', nargs=3, type=float, prompt=True, prompt_required=False,
              help='Position E in format x y z')
@click.option('--position_c', '--pos-c', nargs=3, type=float, prompt=True, prompt_required=False,
              help='Position C in format x y z')
@click.option('--lambda_ab', '-lab', nargs=3, type=float, prompt=True, prompt_required=False,
              help='Position C in format x y z')
@click.option('--lambda_cd', '-lcd', nargs=3, type=float, prompt=True, prompt_required=False,
              help='Position C in format x y z')
@click.option('--upper_range', '-ur', type=float, prompt=True, prompt_required=False,
              help='Position C in format x y z')
@click.option('--lower_range', '-lr', type=float, prompt=True, prompt_required=False,
              help='Position C in format x y z')
@click.option('--step', type=float, prompt=True, prompt_required=False, default=1.0, help='Position C in format x y z')
def exercise_three_c_6(position_a: tuple, position_e: tuple, position_c: tuple, lambda_ab: tuple, lambda_cd: tuple,
                       upper_range: float, lower_range: float, step: float, from_config: bool):


    problem_instance = ThreeCSix(array(position_a), array(position_e), array(position_c), array(lambda_ab), array(lambda_cd), upper_range,
              lower_range, step)

    result = problem_instance.solve()
    print(result)

