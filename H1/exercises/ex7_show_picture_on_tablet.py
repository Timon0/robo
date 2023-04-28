import time
from camera import Camera
from pepper_robots import Robot, PepperConfiguration, PepperNames
from tablet import Tablet
from file_transfer import FileTransfer


config = PepperConfiguration(PepperNames.Pale)
robot = Robot(config)
camera = Camera(robot)

# move it up and down
#robot.ALMotion.setAngles('HeadPitch', 20 * almath.TO_RAD, fractionMaxSpeed=0.2)
#time.sleep(2)

# take a picture
remote_folder_path = "/opt/aldebaran/www/apps/"
file_name = "i_see.jpg"
camera.take_picture(remote_folder_path, file_name)

# show image on tablet
tablet = Tablet(robot)
tablet.show_image(file_name)
time.sleep(5)
tablet.hide_image()

# copy to local filesystem
local = "C:\\Users\\timon\\Documents\\hslu\\06\\ROBO\\Pepper\\" + file_name
remote = remote_folder_path + file_name
file_transfer = FileTransfer(robot)
file_transfer.get(remote, local)
file_transfer.close()
