from pepper_robots import Robot, PepperConfiguration, PepperNames
from camera import Camera
from file_transfer import FileTransfer

config = PepperConfiguration(PepperNames.Amber)
robot = Robot(config)
camera = Camera(robot)

# take a picture


# copy file to local path
