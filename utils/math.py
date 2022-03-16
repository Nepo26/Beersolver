import logging

from numpy import ndarray, arccos, vdot, linalg, rad2deg
from utils import log


def angle_between_vectors(vector_a: ndarray, vector_b: ndarray):
    return rad2deg(arccos(vdot(vector_a, vector_b) / vdot(linalg.norm(vector_a), linalg.norm(vector_b))))


def is_parallel(vector_a: ndarray, vector_b: ndarray):
    theta = angle_between_vectors(vector_a, vector_b)
    log.log_general(f"Angle between {vector_a} and {vector_b} is {theta}", logging.DEBUG)

    if theta == 0.0 or theta == 180.0:
        return True
    else:
        return False
