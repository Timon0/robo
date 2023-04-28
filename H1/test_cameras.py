import time
import almath
import vision_definitions

from exercises.camera import Camera
from exercises.file_transfer import FileTransfer
from pepper_robots import Robot, PepperConfiguration, PepperNames

config = PepperConfiguration(PepperNames.Pale)
robot = Robot(config)
camera = Camera(robot)

robot.ALBasicAwareness.stopAwareness()
robot.ALMotion.setAngles('HeadPitch', 5 * almath.TO_RAD, fractionMaxSpeed=0.3)
robot.ALMotion.setAngles('HeadYaw', 0 * almath.TO_RAD, fractionMaxSpeed=0.3)

camera_definitions = {
    'top': vision_definitions.kTopCamera,
    'bottom': vision_definitions.kBottomCamera,
    'depth': vision_definitions.kDepthCamera,
    'stereo': vision_definitions.kStereoCamera
}

time_stamp = time.time()

for (camera_name, camera_id) in camera_definitions.items():
    print(camera_id)
    print(camera_name)
    camera.configure_camera(camera_id, vision_definitions.k4VGA, "jpg")

    # take a picture
    remote_folder_path = "/opt/aldebaran/www/apps/"
    file_name = str(time_stamp) + "_camera_test_" + camera_name + ".jpg"
    camera.take_picture(remote_folder_path, file_name)

    # copy to local filesystem
    local = "C:\\Users\\timon\\Documents\\hslu\\06\\ROBO\\Pepper\\camera_tests\\" + file_name
    print(local)
    remote = remote_folder_path + file_name
    file_transfer = FileTransfer(robot)
    file_transfer.get(remote, local)
    file_transfer.close()
