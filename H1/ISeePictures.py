import time

import almath

from exercises.camera import Camera
from exercises.file_transfer import FileTransfer
from exercises.tablet import Tablet


class ISeePictures:

    __show_images_on_tablet = False
    __local_folder_path = "C:\\Users\\timon\\Documents\\hslu\\06\\ROBO\\Pepper\\"
    __head_yaw_angles = [-60, 0, 60]

    def __init__(self, robot):
        self.__robot = robot
        self.__camera = Camera(robot)

    def take_pictures(self):
        picture_locations = []

        for head_yaw_angle in self.__head_yaw_angles:
            # move the head into position
            self.__robot.ALMotion.setAngles('HeadPitch', 5 * almath.TO_RAD, fractionMaxSpeed=0.3)
            self.__robot.ALMotion.setAngles('HeadYaw', head_yaw_angle * almath.TO_RAD, fractionMaxSpeed=0.3)
            time.sleep(2)

            # take a picture
            remote_folder_path = "/opt/aldebaran/www/apps/"
            file_name = "i_see" + str(head_yaw_angle) + ".jpg"
            self.__camera.take_picture(remote_folder_path, file_name)

            # show image on tablet
            if self.__show_images_on_tablet:
                tablet = Tablet(self.__robot)
                tablet.show_image(file_name)
                time.sleep(5)
                tablet.hide_image()

            # copy to local filesystem
            local_full_path = self.__local_folder_path + file_name
            remote_full_path = remote_folder_path + file_name
            file_transfer = FileTransfer(self.__robot)
            file_transfer.get(remote_full_path, local_full_path)
            file_transfer.close()

            picture_locations.append(local_full_path)

        return picture_locations

