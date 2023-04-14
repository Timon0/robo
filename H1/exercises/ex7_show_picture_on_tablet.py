import time

from camera import Camera
from pepper_robots import Robot, PepperConfiguration, PepperNames
from tablet import Tablet
from file_transfer import FileTransfer

config = PepperConfiguration(PepperNames.Pale)
robot = Robot(config)
camera = Camera(robot)

# take a picture
remote_folder_path = "/opt/aldebaran/www/apps/"
file_name = "my_picture_14_04_2023-2.jpg"
camera.take_picture(remote_folder_path, file_name)

# show image on tablet
tablet = Tablet(robot)
tablet.show_image(file_name)
time.sleep(5)
tablet.hide_image()
tablet.close()

# copy to local filesystem
local = "C:\\Users\\timon\\Documents\\hslu\\06\\ROBO\\Pepper\\" + file_name
remote = remote_folder_path + file_name
file_transfer = FileTransfer(robot)
file_transfer.get(remote, local)
file_transfer.close()
