import time

from pepper_robots import PepperConfiguration, PepperNames, Robot


class Music():

    def __init__(self, robot):
        self.__audio_player = robot.ALAudioPlayer
        self.__file_id = self.__audio_player.loadFile("/home/nao/waiting-music.wav")

    def play(self):
        self.__audio_player.play(self.__file_id)

    def stop(self):
        self.__audio_player.stopAll()



if __name__ == "__main__":

    config = PepperConfiguration(PepperNames.Pale)
    robot = Robot(config)
    music = Music(robot)
    print('loaded')

    # music.play()

    time.sleep(1)

    music.stop()