# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from dataclasses import dataclass

import numpy as np
import matplotlib as mpl

mpl.use("WXAgg")
from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle, PathPatch
import mpl_toolkits.mplot3d.art3d as art3d
from mpl_toolkits.mplot3d import Axes3D


@dataclass
class img_config:
    axes: any


@dataclass
class coordinates:
    x: float
    y: float
    z: float


def figure_configure(coord: coordinates) -> img_config:
    EXTRA = 5
    x = coord.x
    y = coord.y
    z = coord.z



    """
    create_graph(depth: float, height: float, width: float)


    Creates a base graph with the defined graph of the exercise

    :param x:
    :param y:
    :param z:
    """
    fig = plt.figure()
    axes = fig.add_subplot(111, projection='3d')

    # p = Rectangle((5, 5), 2, 2)
    # ax.add_patch(p)
    #
    # art3d.pathpatch_2d_to_3d(p, z=0, zdir="x")

    axes.set_xlim(0, x + EXTRA)
    axes.set_ylim(0, y + EXTRA)
    axes.set_zlim(0, z + EXTRA)

    return img_config(axes)


def create_frontal_wall(fig_config: img_config, coord: coordinates):
    x = coord.x
    y = coord.y
    z = coord.z

    cube_axes = [x, y, z]

    data = np.ones(cube_axes)
    # Not use voxels as it makes it too slow
    fig_config.axes.voxels(data, edgecolors='grey')

    plt.show()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Starting test...")

    wall_width = 4
    coordinates = coordinates(120, 100, 96)

    fig_config = figure_configure(coordinates)

    create_frontal_wall(fig_config, coordinates)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
