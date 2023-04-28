import time

from ISeePictures import ISeePictures
from image.imagerecognition import ImageRecognition
from music import Music
from pepper_robots import Robot, PepperConfiguration, PepperNames
from game import Game

session_id = 88
config = PepperConfiguration(PepperNames.Pale)
robot = Robot(config)
image_recognition = ImageRecognition()
i_see_pictures = ISeePictures(robot)
game = Game(robot, session_id)
music = Music(robot)

# person identification
robot.ALBasicAwareness.startAwareness()

robot.ALTextToSpeech.say("Welcome to the game!")

started = game.start_game()
play_again = False

# take pictures
while started or play_again:
    robot.ALBasicAwareness.stopAwareness()
    time.sleep(1)
    robot.ALTextToSpeech.say("Wait a second while I scan the room for some objects.")
    music.play()
    picture_locations = i_see_pictures.take_pictures()
    selected_object, selected_object_parent = image_recognition.get_object_from_selection(picture_locations)
    music.stop()
    print(selected_object, selected_object_parent)

    robot.ALBasicAwareness.startAwareness()
    robot.ALTextToSpeech.say("I found an object. Let's start guessing!")

    # guessing dialog
    game.play(selected_object, selected_object_parent)

    # want to play again?
    play_again = game.play_again()
    started = False
