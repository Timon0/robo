
class Accelerometer:
    basePath = lambda sensor: "Device/SubDeviceList/InertialSensorBase/" + sensor + "/Sensor/Value"
    accX = basePath("AccelerometerX")
    accY = basePath("AccelerometerY")
    accZ = basePath("AccelerometerZ")

    angleX = basePath("AngleX")

    def __init__(self, robot):
        self.robot = robot

    def run_demo(self):
        err = robot.ALMemory.subscriber("ALMotion/MoveFailed")
        err.signal.connect(self.errCallback)

        fig, ax = plt.subplots(3)
        x = []
        y = []
        z = []
        idx = []
        for i in range(100):
            self.move()
            x.append(robot.ALMemory.getData(self.accX))
            y.append(robot.ALMemory.getData(self.accY))
            z.append(robot.ALMemory.getData(self.accZ))
            idx.append(i)
            ax[0].plot(idx, x, "ro-")
            ax[1].plot(idx, y, "go-")
            ax[2].plot(idx, z, "bo-")
            plt.pause(0.001)

    def errCallback(self, value):
        print(value[0])

    def move(self):
        if(not robot.ALMotion.moveIsActive()):
            robot.ALMotion.move(0.5, 0.0, 0.0)

if __name__ == '__main__':
    config = PepperConfiguration(PepperNames.Ale)
    robot = Robot(config)
    accelerometer = Accelerometer(robot)
    accelerometer.run_demo()