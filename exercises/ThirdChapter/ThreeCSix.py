"""Exercise ThirdChapter"""
import logging
from configparser import ConfigParser
from dataclasses import dataclass, field

from numpy import array, ndarray, arange, sqrt, vdot, cross
from utils.log import log_general
from utils.math import is_parallel


@dataclass
class Result:
    """
    Object that encapsulates the distance results

        Params
        ------
        distance: float
            distance between E and the line DB
        ab_length: float
            current length of AB
        cd_length: float
            current length of CD
    """
    distance: float = field(default=None)
    ab_length: float = field(default=None)
    cd_length: float = field(default=None)

    def __str__(self):
        return f'({self.distance},{self.ab_length},{self.cd_length})'


@dataclass
class Resolution:
    """
    General object for resolutions. Here we should be able to use the results
    """
    raw_results = list()
    result = Result

    def plot(self):
        pass

    def get_config(self):
        pass


@dataclass
class ThreeCSix(Resolution):
    """
    Produce an object of the problem ThirdChapter.

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
        get_minimal_distance()

        calculate_distance_e_db()

        solve()

        Examples
        --------
        Solve the problem with the default values

        >> from numpy import array
        >> a = ThirdChapter(
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

    # a

    # Position of the first duct
    position_a: ndarray = field(default=array([0.0, 96.0, 4.0]))

    # Position of the thermometer
    position_e: ndarray = field(default=array([90.0, 52.0, 0.0]))

    # Position of the second duct
    position_c: ndarray = field(default=array([120.0, 36.0, 100.0]))

    lambda_ab: ndarray = field(default=array([7 / 9, -4 / 9, 4 / 9]))
    lambda_cd: ndarray = field(default=array([-7 / 9, 4 / 9, -4 / 9]))

    upper_range: float = field(default=36.0)
    lower_range: float = field(default=9.0)

    range: ndarray = field(init=False)

    step: float = field(default=1.0)

    def __post_init__(self):
        self.range = arange(self.lower_range, self.upper_range + self.step, self.step)

        # Check if lambda_ab and lambda_cd are parallels
        if not is_parallel(self.lambda_ab, self.lambda_cd):
            log_general(f"{self.lambda_ab} and {self.lambda_cd} are not parallel", logging.DEBUG)

            raise Exception(f"{self.lambda_ab} and {self.lambda_cd} are not parallel")

    @staticmethod
    def get_minimal_distance(values: list[Result]) -> Result:
        """
        Get minimal distance on a list of results
        :param values: list of results from the distance of e from the line DB
        :type values: list[Result]
        """
        minimal_result = None

        for value in values:
            log_general(str(value), logging.DEBUG)

            dist = value.distance
            ab_length = value.ab_length
            cd_length = value.cd_length

            if minimal_result is None:
                minimal_result = Result(dist, ab_length, cd_length)

            if dist < minimal_result.distance:
                minimal_result.distance = dist
                minimal_result = Result(dist, ab_length, cd_length)

        log_general(f"minimal_distance: {minimal_result}", logging.DEBUG)
        return minimal_result

    def calculate_distance_e_db(self, ab_length: float, cd_length: float) -> Result:
        """
        Calculate the distance between the E point and the line DB
        :param ab_length: the current length of AB
        :type ab_length: float
        :param cd_length: the current length of CD
        :type cd_length: float
        :return: Result(a,b,distance)
        """

        # Get the vector for the value of AB over the unitary vector lambda AB
        ab_vector = ab_length * self.lambda_ab
        log_general(f"ab_vector = {ab_vector}", logging.DEBUG)

        # Get the vector for the value of C over the unitary vector lambda CD
        cd_vector = cd_length * self.lambda_cd
        log_general(f"cd_vector = {cd_vector}", logging.DEBUG)

        r_a = self.position_a
        r_c = self.position_c
        r_e = self.position_e
        log_general(f"r_a = {r_a}", logging.DEBUG)
        log_general(f"r_c = {r_c}", logging.DEBUG)
        log_general(f"r_e = {r_e}", logging.DEBUG)

        # Get r_b and r_d
        r_b = ab_vector + r_a
        r_d = cd_vector + r_c
        log_general(f"r_b = {r_b}", logging.DEBUG)
        log_general(f"r_d = {r_d}", logging.DEBUG)

        # Get r_db and r_de
        r_db = r_b - r_d
        r_de = r_e - r_d

        log_general(f"r_db = {r_db}", logging.DEBUG)
        log_general(f"r_de = {r_db}", logging.DEBUG)

        # Get the lambda DB value
        lambda_db = r_db / (sqrt(vdot(r_db, r_db)))
        log_general(f"λ_db = {lambda_db}", logging.DEBUG)

        line_e = cross(lambda_db, r_de)
        log_general(f"line_e = {line_e}", logging.DEBUG)

        # Get the distance of the E Point to the DB line
        distance_e = sqrt(vdot(line_e, line_e))

        return Result(distance_e, ab_length, cd_length)

    def get_config(self) -> ConfigParser:
        config = ConfigParser()

        config["positions"] = {
            "a": self.position_a,
            "b": self.position_b,
            "c": self.position_c,
        }

        config["lambdas"] = {
            "lambda_ab": self.lambda_ab,
            "lambda_cd": self.lambda_cd
        }

        config["range"] = {
            "upper_range": self.upper_range,
            "lower_range": self.upper_range,
            "step": self.step
        }

        return config

    def solve(self) -> Result:
        """
        Solves the basic exercise and set the results' field
        :return: Result
        """

        # Loops by all possibilites for the size of a and c determined by the range
        values = []
        for ab_length in self.range:
            for cd_length in self.range:
                distance_e = self.calculate_distance_e_db(ab_length, cd_length)

                values.append(Result(distance_e.distance, ab_length, cd_length))

        self.raw_results = values

        self.result = self.get_minimal_distance(values)

        return self.result


# exercise = ThreeCSix()
# distance = exercise.calculate_distance_e_db(9, 9)
# print(distance)
#
# exercise = ThreeCSix()
# print(exercise.solve())
