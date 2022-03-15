"""Exercise 3C.6"""

from dataclasses import dataclass, field
from pprint import pprint

import numpy as np
from numpy import array, ndarray, arange


@dataclass
class Result:
    """
    Object that encapsulates the distance results

        Params
        ------
        distance: float
            distance between E and the line DB
        a: float
            current value of a
        c: float
            current value of c
    """
    distance: float = field(default=None)
    a: float = field(default=None)
    c: float = field(default=None)

    def __str__(self):
        return f'({self.distance},{self.a},{self.c})'


@dataclass
class Resolution:
    """
    General object for resolutions. Here we should be able to use the results
    """
    raw_results = list()
    result = Result

    def plot(self):
        pass


@dataclass
class ThreeCSix(Resolution):
    """
    Produce an object of the problem 3C.6.

        Parameters
        ----------

        position_a: ndarray
            position A, position of the first(upper) duct
        position_e: ndarray
            position E, position of the thermometer
        position_c: ndarray
            position C, position of the second(lower) duct
        lambda_ab: ndarray
            unitary vector AB
        lambda_cd: ndarray
            unitary vector CD
        upper_range: float
            upper part of the range that determines the size of A and the size C
        lower_range: float
            lower part of the range that determines the size of A and the size C
        step: float,optional
            step to mve on the range, also determines the precision of the answer

        Methods
        -------

        Examples
        --------
        Solve the problem with the default values

        >> from numpy import array
        >> a = ThreeCSix(
                array([0.0, 4, 96]),
                array([90.0, 52.0, 0.0]),
                array([120.0, 36.0, 100.0]),
                array([7/9, -4/9, 4/9]),
                array([-7/9, 4/9, -4/9]),
                36.0,
                9.0
            )
        >> print(a.solve())

        (80.67809762705207,36.0,36.0)
    """
    # Unit
    # TODO Implement conversion and use of [pint](https://pint.readthedocs.io/en/0.6/numpy.html)

    # Position of the first duct
    position_a: ndarray = field(default=array([0.0, 96.0, 4.0]))

    # Position of the thermometer
    position_e: ndarray = field(default=array([90.0, 52.0, 4.0]))

    # Position of the second duct
    position_c: ndarray = field(default=array([120.0, 36.0, 100.0]))

    lambda_ab: ndarray = field(default=array([7/9, -4/9, 4/9]))
    lambda_cd: ndarray = field(default=array([-7/9, 4/9, -4/9]))

    upper_range: float = field(default=36.0)
    lower_range: float = field(default=9.0)

    range: ndarray = field(init=False)

    step: float = field(default=1.0)

    def __post_init__(self):
        self.range = arange(self.lower_range, self.upper_range + self.step, self.step)

    @staticmethod
    def get_minimal_distance(values: list[Result]) -> Result:
        """
        Get minimal distance on a list of results
        :param values: list of results from the distance of e from the line DB
        :type values: list[Result]
        """
        largest_info = None

        pprint(values)
        pass
        for value in values:
            distance = value['distance']
            a = value['a']
            c = value['c']

            if largest_info is None:
                largest_info = Result(distance, a, c)

            if distance < largest_info.distance:
                largest_info.distance = distance
                largest_info = Result(distance, a, c)

        return largest_info

    def calculate_distance_e_db(self, a: float, c: float) -> Result:
        """
        Calculate the distance between the E point and the line DB

        :param a: the current size of a
        :type a: float
        :param c: the current size of e
        :type c: float
        :return: Result(a,b,distance)
        """

        a_value = a
        c_value = a


        # Get the vector for the value of A over the unitary vector lambda AB
        a *= self.lambda_ab

        # Get the vector for the value of C over the unitary vector lambda CD
        c *= self.lambda_cd

        r_a = self.position_a
        r_c = self.position_c
        r_e = self.position_e

        # Get r_b and r_d
        r_b = a + r_a
        r_d = c + r_c

        # Get r_db and r_de
        r_db = r_b - r_d
        r_de = r_e - r_d

        # Get the lambda DB value
        lambda_db = r_db / (np.sqrt(np.vdot(r_db, r_db)))

        line_e = np.cross(lambda_db, r_de)

        # Get the distance of the E Point to the DB line
        distance_e = np.sqrt(np.vdot(line_e, line_e))

        return Result(distance_e, a_value, c_value)

    def solve(self):
        """
        Solves the basic exercise and set the results' field
        :return: Result
        """

        # Loops by all possibilites for the size of a and c determined by the range
        values = []
        for a in self.range:
            for c in self.range:
                distance_e = self.calculate_distance_e_db(a, c)

                values.append({"distance": distance_e.distance, "a": distance_e.a, "c": distance_e.c})

        self.raw_results = values

        self.result = self.get_minimal_distance(values)

        return self.result

a = ThreeCSix(
    array([0.0, 4, 96]),
    array([90.0, 52.0, 0.0]),
    array([120.0, 36.0, 100.0]),
    array([7/9, -4/9, 4/9]),
    array([-7/9, 4/9, -4/9]),
    36.0,
    9.0
)

print(a.solve())