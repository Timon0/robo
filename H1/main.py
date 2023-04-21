import time

from ISeePictures import ISeePictures
from image.imagerecognition import ImageRecognition
from pepper_robots import Robot, PepperConfiguration, PepperNames

config = PepperConfiguration(PepperNames.Pale)
robot = Robot(config)
image_recognition = ImageRecognition()
i_see_pictures = ISeePictures(robot)

# person identification
robot.ALBasicAwareness.startAwareness()

# TODO: Welcome dialog
robot.ALTextToSpeech.say("Welcome to the game!")
time.sleep(10)


# take pictures
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
