import time

from camera import Camera
from pepper_robots import Robot, PepperConfiguration, PepperNames
from tablet import Tablet

config = PepperConfiguration(PepperNames.Pale)
robot = Robot(config)
camera = Camera(robot)

# take a picture
remote_folder_path = "/opt/aldebaran/www/apps/"
file_name = "my_picture_14_04_2023-1.jpg"
camera.take_picture(remote_folder_path, file_name)

tablet = Tablet(robot)

try:
    tablet.show_image(file_name)
    time.sleep(5)
    tablet.hide_image()
    tablet.close()
except RuntimeError, e:
    print "error in showing image on tablet", e