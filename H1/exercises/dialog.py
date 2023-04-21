import time


class Dialog:

    def __init__(self, robot):
        self.__al_mem = robot.ALMemory
        self.subscriber = self.__al_mem.subscriber('WordRecognized')
        self.subscriber.signal.connect(self.callback)
        self.__al_tts = robot.ALTextToSpeech
        self.__al_sr = robot.ALSpeechRecognition
        self.topics = {}

    def say(self, text):
        self.__al_tts.say(text)

    def say_slowly(self, text):
        self.__al_tts.setParameter('speed', 50)
        self.__al_tts.say(text)
        self.__al_tts.setParameter('speed', 100)

    def shout(self, text):
        oldVolume = self.__al_tts.getVolume()
        self.__al_tts.setVolume(2)
        self.__al_tts.say(text)
        self.__al_tts.setVolume(oldVolume)

    def add_simple_reaction(self, topic_name, user_input, robot_output):
        self.topics[topic_name].append({
            'input': user_input,
            'output': robot_output,
            'type': 'simple_reaction'
        })
        self.__al_sr.setVocabulary(user_input.split(), False)

    def load_yes_no_question(self, topic_name, question, reaction_yes, reaction_no):
        # to be implemented
        self.topics[topic_name].append({
            'question': question,
            'yes_reaction': reaction_yes,
            'no_reaction': reaction_no,
            'type': 'yes_no_question'
        })
        self.__al_sr.pause(True)
        self.__al_sr.setVocabulary(['yes', 'no'], False)
        self.__al_sr.pause(False)

    def ask_yes_no_question(self, topic):
        question_info = self.topics[topic]
        if question_info[0]['type'] == 'yes_no_question':
            self.say(question_info[0]['question'])

    def add_topic(self, topic_name):
        self.topics[topic_name] = []

    def start_topic(self, topic_name):
        self.__al_sr.subscribe(topic_name, 1, 0.2)

    def stop_topic(self, topic_name):
        self.__al_sr.unsubscribe(topic_name)

    def close_session(self):
        self.topics = {}

    def callback(self, value):
        print(value)

        for topic, array in self.topics.items():
            for input in array:
                if input['type'] == 'simple_reaction':
                    if value[0] == input['input'] and value[1] > 0.35:
                        self.say(input['output'])
                elif input['type'] == 'yes_no_question':
                    if value[0] == 'yes' and value[1] > 0.35:
                        self.say(input['yes_reaction'])
                    elif value[0] == 'no' and value[1] > 0.35:
                        self.say(input['no_reaction'])