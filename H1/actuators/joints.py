from pepper_robots import Robot, PepperConfiguration, PepperNames


class Joints:
    def __init__(self, robot):
        self.robot = robot

    def run_demo(self):
        self.robot.ALMotion.wakeUp()
        
        joint_names = self.robot.ALMotion.getBodyNames("JointActuators")
        print (joint_names)

        # move non blocking
        self.robot.ALTextToSpeech.say("move non blocking")
        self.robot.ALMotion.setAngles("HipRoll", 0.5, 0.1)

        # move blocking
        self.robot.ALTextToSpeech.say("move blocking")
        self.robot.ALMotion.angleInterpolationWithSpeed(["LShoulderRoll", "RShoulderRoll"], [1, -1], 0.1)

        # move to limits
        self.robot.ALTextToSpeech.say("move to 70% of limits")
        pos_limit = 0.7
        limits = []
        for joint in joint_names:
            limits.append(self.robot.ALMotion.getLimits(joint)[0][1] * pos_limit)
        self.robot.ALMotion.angleInterpolationWithSpeed(joint_names, limits, 0.2)
        limits = []
        for joint in joint_names:
            limits.append(self.robot.ALMotion.getLimits(joint)[0][0] * pos_limit)
        self.robot.ALMotion.angleInterpolationWithSpeed(joint_names, limits, 0.2)

        # postures
        self.robot.ALTextToSpeech.say("move to postures")
        self.robot.ALRobotPosture.goToPosture("StandInit", 0.5)
        self.robot.ALRobotPosture.goToPosture("StandZero", 0.5)
        self.robot.ALRobotPosture.goToPosture("Crouch", 0.5)
        self.robot.ALRobotPosture.goToPosture("StandInit", 0.5)


if __name__ == '__main__':
    config = PepperConfiguration(PepperNames.Amber)
    robot = Robot(config, reset=True)
    joints = Joints(robot)
    joints.run_demo()
