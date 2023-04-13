from pepper_robots import Robot, PepperConfiguration, PepperNames
import matplotlib.pyplot as plt

class Gyroscope:
    basePath = lambda sensor: "Device/SubDeviceList/InertialSensorBase/" + sensor + "/Sensor/Value"
    gyroX = basePath("GyroscopeX")
    gyroY = basePath("GyroscopeY")
    gyroZ = basePath("GyroscopeZ")

    def __init__(self, robot):
        self.robot = robot

    def run_demo(self):
        fig, ax = plt.subplots(3)
        x = []
        y = []
        z = []
        idx = []
        for i in range(100):
            x.append(robot.ALMemory.getData(self.gyroX))
            y.append(robot.ALMemory.getData(self.gyroY))
            z.append(robot.ALMemory.getData(self.gyroZ))
            idx.append(i)
            ax[0].plot(idx, y, "ro-")
            ax[1].plot(idx, x, "go-")
            ax[2].plot(idx, z, "bo-")
            plt.pause(0.001)


if __name__ == '__main__':
    config = PepperConfiguration(PepperNames.Ale)
    robot = Robot(config)
    gyro = Gyroscope(robot)
    gyro.run_demo()
