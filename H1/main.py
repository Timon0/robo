import time

from ISeePictures import ISeePictures
from image_recognition.imagerecognition import ImageRecognition
from pepper_robots import Robot, PepperConfiguration, PepperNames
from game import Game

session_id = 88
config = PepperConfiguration(PepperNames.Pale)
robot = Robot(config)
image_recognition = ImageRecognition()
i_see_pictures = ISeePictures(robot)
game = Game(robot, session_id)

# person identification
robot.ALBasicAwareness.startAwareness()

# TODO: Welcome dialog
robot.ALTextToSpeech.say("Welcome to the game!")
#time.sleep(10)

started = game.start_game()

# take pictures
if started:
    robot.ALBasicAwareness.stopAwareness()
    robot.ALTextToSpeech.say("Wait a second while I scan the room for some objects.")
    picture_locations = i_see_pictures.take_pictures()
    selected_object, selected_object_parent = image_recognition.get_object_from_selection(picture_locations)

# todo: guessing dialog

# todo: maybe add hint if parent of object is available


# todo: want to play again?

print(picture_locations)
print(selected_object)
print(selected_object_parent)
