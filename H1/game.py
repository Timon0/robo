import time


class Game():

    def __init__(self, robot, session_id):
        self.session_id = session_id
        self.robot = robot
        self.dialog_name = 'game_dialog'
        self.dialog = self.robot.session.service('ALDialog')
        self.dialog.openSession(self.session_id)
        self.textToSpeech = self.robot.session.service("ALTextToSpeech")
        self.textToSpeech.setLanguage("English")

        self.game_started = False

        self._current_topic_name = None
        self._current_used_variables = []

    def __del__(self):
        self.dialog.closeSession(self.session_id)

    def read_variable(self, name):
        if name not in self._current_used_variables:
            self._current_used_variables.append(name)

        return self.dialog.getUserData(name, self.session_id)
    
    def load_topic(self, name, content):
        self.dialog.loadTopicContent(content)
        self.dialog.activateTopic(name)

        self.dialog.subscribe(self.dialog_name)
        self.dialog.setFocus(name)
        self.dialog.forceOutput()

    def start_game(self):
        topic_start = open('./dialog_files/game_start.txt').read()
        topic_name = 'start_game'

        self.load_topic(topic_name, topic_start)

        start = 0

        while start not in ['0', '1']:
            start = self.read_variable('start')
            time.sleep(1)

        if start == '1':
            self.game_started = True
        elif start == '0':
            self.game_started = False

        return self.game_started