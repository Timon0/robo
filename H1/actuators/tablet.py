from pepper_robots import Robot, PepperConfiguration, PepperNames


class Tablet:
    def __init__(self, robot):
        self.robot = robot

    def run_demo(self):
        # Copy the folder content tablet/html in boot-config/html folder on the robot
        self.robot.ALTabletService.showWebview("http://198.18.0.1/boot-config/html/index.html")
        pass


if __name__ == '__main__':
    config = PepperConfiguration(PepperNames.Amber)
    robot = Robot(config)
    tablet = Tablet(robot)
    tablet.run_demo()
