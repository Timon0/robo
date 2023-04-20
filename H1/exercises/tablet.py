import qi
import os
import shutil


class Tablet:

    def __init__(self, robot):
        self.__al_tablet_service = robot.session.service("ALTabletService")
        pass

    def show_image(self, file):
        self.__al_tablet_service.showImageNoCache("http://198.18.0.1/apps/" + file)

    def hide_image(self):
        self.__al_tablet_service.hideImage()
