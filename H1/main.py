from ISeePictures import ISeePictures
from image_recognition.imagerecognition import ImageRecognition
from pepper_robots import Robot, PepperConfiguration, PepperNames

config = PepperConfiguration(PepperNames.Pale)
robot = Robot(config)
image_recognition = ImageRecognition()

i_see_pictures = ISeePictures(robot)
picture_locations = i_see_pictures.take_pictures()

print(picture_locations)
print(image_recognition.get_object_from_selection(picture_locations))
