import almath

from pepper_robots import Robot, PepperConfiguration, PepperNames


class Wheels:
    def __init__(self, robot):
        self.robot = robot

    def run_demo(self):
        tts = self.robot.ALAnimatedSpeech  # text to speech service
        tts.say("Let me show you how my wheels work")

        success = self.robot.ALMotion.moveTo(0.5, 0, 0)
        success = self.robot.ALMotion.moveTo(-0.5, 0, 0) and success
        success = self.robot.ALMotion.moveTo(0, -0.5, 0) and success
        success = self.robot.ALMotion.moveTo(x=0, y=0, theta=360 * almath.TO_RAD) and success
        success = self.robot.ALMotion.moveTo(0, 0.5, 0) and success

        if not success:
            tts.say("Oh no! Something went wrong during my demonstration")


if __name__ == '__main__':
    config = PepperConfiguration(PepperNames.Amber)
    robot = Robot(config)
    wheels = Wheels(robot)
    wheels.run_demo()
