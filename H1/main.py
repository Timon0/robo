from ISeePictures import ISeePictures
from image_recognition.imagerecognition import ImageRecognition
from pepper_robots import Robot, PepperConfiguration, PepperNames

config = PepperConfiguration(PepperNames.Pale)
robot = Robot(config)
image_recognition = ImageRecognition()
i_see_pictures = ISeePictures(robot)

# TODO: Welcome dialog

picture_locations = i_see_pictures.take_pictures()
selected_object, selected_object_parent = image_recognition.get_object_from_selection(picture_locations)

# TODO: Guessing dialog

# TODO: Maybe add hint if parent of object is available

print(picture_locations)
print(selected_object)
print(selected_object_parent)
