from camera import Camera
from pepper_robots import Robot, PepperConfiguration, PepperNames

config = PepperConfiguration(PepperNames.Amber)
robot = Robot(config)
camera = Camera(robot)

# take a picture


# copy file to local path
