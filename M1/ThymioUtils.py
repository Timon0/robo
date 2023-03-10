import math


class Thymio:

    @staticmethod
    def mms_to_thymio(v: float) -> int:
        """
        Calculate the internal Thymio distance based on the velcocity in mm/s

        :param v: velocity in mm/s
        :return:
        """
        v_thymio = v * 3.3
        return min(math.floor(v_thymio), 500)

    @staticmethod
    def curve_velocity(self, r: float, v: float) -> tuple[int, int]:
        """
        Calculate velocity for each wheel to drive a certain curve.

        :param r: radius of the curve
        :param v: velocity in mm/s
        :return: velocity for each wheel
        """
        w = v / r
        v_inner = w * (r - 105 / 2)
        v_outer = w * (r + 105 / 2)
        return self.mms_to_thymio(v_inner), self.mms_to_thymio(v_outer)

    @staticmethod
    def time_for_distance(d: float, v: float):
        """
        Calculate the time for driving a certain distance at a constant velocity.

        :param d: distance
        :param v: velocity in mm/s
        :return: time
        """

        return d / v

    @staticmethod
    def time_for_circle(self, r, v, degrees=360, error_full_circle=0.3):
        """
        Calculate the time for driving a certain circle at a constant velocity.

        :param r: radius of the circle
        :param v: velocity in mm/s
        :param degrees: degrees of circle
        :param error_full_circle: error term in seconds for a full circle
        :return: velocity for each wheel
        """
        percentage_of_circle = degrees/360
        return (self.time_for_distance(2 * r * math.pi, v) + error_full_circle) * percentage_of_circle
    
    @staticmethod
    def time_for_spin(speed, deg, error=0.15):
        percentage = deg / 360
        dist = math.floor((301 / 360) * deg)
        return (dist / speed) - (percentage * error)
