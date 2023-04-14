import requests
import json


class ImageRecognition:
    __endpoint = 'https://pepper-image-recognition.cognitiveservices.azure.com'
    __model_version = 'latest'

    def __init__(self):
        with open("../config/config.json", "r") as jsonfile:
            data = json.load(jsonfile)
            self.__subscription_key = data['imagerecognition']['subscription_key']

    def get_objects(self, image_data):
        url = self.__endpoint + '/vision/v3.2/detect?model-version' + self.__model_version
        headers = {
            'Ocp-Apim-Subscription-Key': self.__subscription_key,
            'Content-Type': 'application/octet-stream'
        }
        response = requests.post(url, headers=headers, data=image_data)
        objects = []

        if response.status_code == 200:
            for obj in response.json()['objects']:
                objects.append(obj['object'])

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
