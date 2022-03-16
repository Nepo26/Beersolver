from numpy import ndarray, arccos, vdot, linalg, rad2deg


def angle_between_vectors(vector_a: ndarray, vector_b: ndarray):
    return rad2deg(arccos(vdot(vector_a, vector_b) / vdot(linalg.norm(vector_a), linalg.norm(vector_b))))


def is_parallel(vector_a: ndarray, vector_b: ndarray):
    theta = angle_between_vectors(vector_a, vector_b)

    if theta is 0.0 or theta is 180.0:
        return True
    else:
        return False
