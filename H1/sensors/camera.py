import vision_definitions

from pepper_robots import Robot, PepperConfiguration, PepperNames
from PIL import Image


class Camera:
    def __init__(self, robot):
        self.robot = robot
        self.__vidDevice = robot.ALVideoDevice
        self.__app_name = 'camera_demo'

    def run_demo(self):
        # Start the camera and subscribe to it
        image_client = self.__vidDevice.subscribeCamera(
            self.__app_name,
            vision_definitions.kDepthCamera,
            vision_definitions.kQVGA,
            vision_definitions.kRGBColorSpace,
            5)

        # Get the latest frame
        result = self.__vidDevice.getImageRemote(image_client)

        # Convert the frame to a PIL image
        image_width = result[0]
        image_height = result[1]
        data = result[6]
        image = Image.frombytes("RGB", (image_width, image_height), str(bytearray(data)))

        # Save and show the image
        image.save("image_depth.jpg")
        image.show()

        # Release the frame and unsubscribe
        self.__vidDevice.releaseImage(image_client)
        self.__vidDevice.unsubscribe(image_client)


if __name__ == '__main__':
    config = PepperConfiguration(PepperNames.Amber)
    robot = Robot(config)
    cam = Camera(robot)
    cam.run_demo()
