import requests
import json
import random
from PIL import Image
import io


class ImageRecognition:
    __endpoint = 'https://pepper-image-recognition.cognitiveservices.azure.com'
    __model_version = 'latest'

    def __init__(self):
        with open("./config/config.json", "r") as jsonfile:
            data = json.load(jsonfile)
            self.__subscription_key = data['imagerecognition']['subscription_key']

    def get_objects(self, image_data):
        url = self.__endpoint + '/vision/v3.2/detect?model-version=' + self.__model_version
        headers = {
            'Ocp-Apim-Subscription-Key': self.__subscription_key,
            'Content-Type': 'application/octet-stream'
        }
        response = requests.post(url, headers=headers, data=image_data)
        objects = []

        if response.status_code == 200:
            for obj in response.json()['objects']:
                obj_found = obj['object']
                parent = None
                while 'parent' in obj:
                    parent = obj['parent']['object']
                    obj = obj['parent']
                objects.append((obj_found, parent))

        return objects

    def describe_image(self, image_data):
        max_candidates = '1'
        language = 'en'
        url = self.__endpoint + "/vision/v3.2/describe?maxCandidates=" + max_candidates + \
            "&language=" + language + \
            "&model-version=" + self.__model_version

        headers = {
            'Ocp-Apim-Subscription-Key': self.__subscription_key,
            'Content-Type': 'application/octet-stream'
        }
        response = requests.post(url, headers=headers, data=image_data)

        description = 'No Description available'
        if response.status_code == 200:
            description = response.json()['description']['captions'][0]['text']

        return description

    def get_object_from_selection(self, image_paths):
        objects = []
        for path in image_paths:
            image = Image.open(path)
            img_width, img_height = image.size

            # [upper left, upper right, lower left, lower right]
            tiles = [image.crop((0, 0, int(img_width * 0.6), int(img_height * 0.6))),
                     image.crop((int(img_width * 0.4), 0, img_width, int(img_height * 0.6))),
                     image.crop((0, int(img_height * 0.4), int(img_width * 0.6), img_height)),
                     image.crop((int(img_width * 0.4), int(img_height * 0.4), img_width, img_height))]

            for i, tile in enumerate(tiles):
                img_byte_arr = io.BytesIO()
                tile.save(img_byte_arr, format='PNG')
                img_byte_arr = img_byte_arr.getvalue()
                found = self.get_objects(img_byte_arr)
                objects.extend(found)

        return random.choice(objects)

    def get_single_object(self, image_data):
        url = self.__endpoint + '/vision/v3.2/detect?model-version' + self.__model_version
        headers = {
            'Ocp-Apim-Subscription-Key': self.__subscription_key,
            'Content-Type': 'application/octet-stream'
        }
        response = requests.post(url, headers=headers, data=image_data)

        obj = 'No object found'
        parent = 'No parent available'
        if response.status_code == 200 and len(response.json()['objects']) > 0:
            rand_index = random.randrange(len(response.json()['objects']))
            object_found = response.json()['objects'][rand_index]
            obj = object_found['object']
            while 'parent' in object_found:
                parent = object_found['parent']['object']
                object_found = object_found['parent']

        return obj, parent
