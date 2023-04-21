from pepper_robots import Robot, PepperConfiguration, PepperNames
from dialog import Dialog
import time

config = PepperConfiguration(PepperNames.Pale)
robot = Robot(config)
dialog = Dialog(robot)


topic_name = "topic_yes_no"
dialog.add_topic(topic_name)
dialog.load_yes_no_question(topic_name, "hello human, are you ready to play a game", "great, let's start the game", "what a pity")
dialog.start_topic(topic_name)

dialog.ask_yes_no_question(topic_name)
time.sleep(20)
dialog.stop_topic(topic_name)

dialog.close_session()