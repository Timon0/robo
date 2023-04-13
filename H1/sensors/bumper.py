from pepper_robots import Robot, PepperConfiguration, PepperNames
import sys

class Bumper:
    """
    Tactile sensor with a callback on sensor changes.
    """
    def __init__(self, robot, tactile_sensor_name, on_sensor_state_changed_func=None):
        """
        Constructor of tactile sensor
        :param robot: The robot instance from pepper.Robot
        :param tactile_sensor_name: A TactileSensorName
        :param on_sensor_state_changed_func: function with following signature: func(sensor_value).
        This function will be called, when the sensor value changes
        """
        self.on_sensor_state_changed_func = on_sensor_state_changed_func
        self.memory = robot.session.service("ALMemory")
        self.subscriber = self.memory.subscriber(tactile_sensor_name)
        self.session_id = sys.maxint

    def set_on_sensor_state_changed_function(self, on_sensor_state_changed_func):
        """
        Sets the callback of sensor state changed
        :param on_sensor_state_changed_func: the function which shall be called, when the sensor state changes
        :return: Returns Boolean which indicates whether the function was settable or not.
        """
        if self.session_id != sys.maxint:
            return False

        self.on_sensor_state_changed_func = on_sensor_state_changed_func
        return True

    def start_listening(self):
        """
        Starts listening for sensor state changes
        """
        if self.on_sensor_state_changed_func is not None \
                and self.session_id == sys.maxint:
            self.session_id = self.subscriber.signal.connect(self.on_sensor_state_changed_func)

    def stop_listening(self):
        """
        Stops listening for sensor state changes
        :return:
        """
        if self.on_sensor_state_changed_func is not None \
                and self.session_id != sys.maxint:
            self.subscriber.signal.disconnect(self.session_id)
            self.session_id = sys.maxint


def on_left_bumper_pressed(val):
    if val == 1:
        tts.say("Left Bumper pressed")
    else:
        tts.say("Left Bumper not pressed")

def on_right_bumper_pressed(val):
    if val == 1:
        tts.say("Right Bumper pressed")
    else:
        tts.say("Right Bumper not pressed")

def on_back_bumper_pressed(val):
    if val == 1:
        tts.say("Back Bumper pressed")
    else:
        tts.say("Back Bumper not pressed")

tts = None

if __name__ == '__main__':
    config = PepperConfiguration(PepperNames.Amber)
    robot = Robot(config)
    tts = robot.session.service("ALTextToSpeech")
    bumperLeft = Bumper(robot, "LeftBumperPressed", on_left_bumper_pressed)
    bumperLeft.start_listening()
    bumperRight = Bumper(robot, "RightBumperPressed", on_right_bumper_pressed)
    bumperRight.start_listening()
    bumperBack = Bumper(robot, "BackBumperPressed", on_back_bumper_pressed)
    bumperBack.start_listening()

    if robot.ALAutonomousLife.getState() != "disabled":
        robot.ALAutonomousLife.setState("disabled")
    robot.ALRobotPosture.goToPosture("Stand", 0.5)

    while True:
        pass
