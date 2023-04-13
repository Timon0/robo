import time

from pepper_robots import Robot, PepperConfiguration, PepperNames


class Microphone:
    def __init__(self, robot):
        self.robot = robot

    def run_demo(self):
        self.robot.ALSoundLocalization.subscribe2("sound_located")

def sound_located(result):
    print("azimuth = " + result[0][0])
    print("elevation = " + result[0][1])
    print("confidence = " + result[0][2])
    print("energy = " + result[0][3])

    print("headPositionTorso = " + result[1])
    print("headPositionRobot = " + result[2])

if __name__ == '__main__':
    config = PepperConfiguration(PepperNames.Amber)
    robot = Robot(config)
    mic = Microphone(robot)
    mic.run_demo()
