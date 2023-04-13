from pepper_robots import Robot, PepperConfiguration, PepperNames


class Laser:
    def __init__(self, _robot):
        self.robot = _robot

    def run_demo(self):
        print("start run_demo")
        self.robot.ALTextToSpeech.say("I start the laser demo")

        self.robot.ALLaser.laserON()

        self.robot.ALTextToSpeech.say("I do now measure the distance to an obstacle")

        x_distance_meter = self.get_x_distance_to_obstacle_front()
        print("measured distance: " + str(x_distance_meter))

        self.robot.ALTextToSpeech.say("I did measure " + str(round(x_distance_meter, 2)) + " meter")
        self.robot.ALTextToSpeech.say("End of the demo")
        print("end run_demo")

    def get_x_distance_to_obstacle_front(self):
        return self.robot.ALMemory.getData("Device/SubDeviceList/Platform/LaserSensor/Front/Horizontal/Seg08/X/Sensor/Value")


if __name__ == '__main__':
    config = PepperConfiguration(PepperNames.Amber)
    robot = Robot(config, reset=True)
    laser = Laser(robot)
    laser.run_demo()
