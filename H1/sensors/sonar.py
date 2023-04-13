from pepper_robots import Robot, PepperConfiguration, PepperNames


class Sonar:
    def __init__(self, robot):
        self.robot = robot

    def run_demo(self):
        self.robot.ALTextToSpeech.say("Start of Sonar Demo")

        distance_front_meter = self.robot.ALMemory.getData('Device/SubDeviceList/Platform/Front/Sonar/Sensor/Value')
        distance_back_meter = self.robot.ALMemory.getData('Device/SubDeviceList/Platform/Back/Sonar/Sensor/Value')

        self.robot.ALTextToSpeech.say("Distance in front is " + format(distance_front_meter, '.2f') + " meter")
        self.robot.ALTextToSpeech.say("Distance behind is " + format(distance_back_meter, '.2f') + " meter")

        self.robot.ALTextToSpeech.say("End of Sonar Demo")


if __name__ == '__main__':
    config = PepperConfiguration(PepperNames.Amber)
    robot = Robot(config)
    sonar = Sonar(robot)
    sonar.run_demo()

