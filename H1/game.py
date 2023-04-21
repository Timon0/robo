import time
from varname import nameof

class Game():

    def __init__(self, robot, session_id):
        self.session_id = session_id
        self.robot = robot
        self._dialog_name = 'game_dialog'
        self.dialog = self.robot.session.service('ALDialog')
        self.dialog.openSession(self.session_id)
        self.textToSpeech = self.robot.session.service("ALTextToSpeech")
        self.textToSpeech.setLanguage("English")

        self.game_started = False

        self._current_topic_name = None
        self._current_used_variables = []

    def __del__(self):
        for topic in self.getLoadedTopics('English'):
            self.unload_topic(topic)

        self.dialog.closeSession()

    def read_variable(self, name):
        if name not in self._current_used_variables:
            self._current_used_variables.append(name)

        return self.dialog.getUserData(name, self.session_id)
    
    def load_topic(self, name, content):
        self.dialog.loadTopicContent(content)
        self.dialog.activateTopic(name)

        self.dialog.subscribe(self._dialog_name)
        self.dialog.setFocus(name)
        self.dialog.forceOutput()

    def unload_topic(self, name):
        try:
            self.dialog.unsubscribe(self._dialog_name)
        except:
            pass
        self.dialog.deactivateTopic(name)
        self.dialog.unloadTopic(name)

    def start_game(self):
        topic_start = open('./dialog_files/game_start.txt').read()
        topic_name = 'start_game'

        self.load_topic(topic_name, topic_start)

        start = 0

        while start not in ['0', '1']:
            start = self.read_variable('start')
            time.sleep(1)

        self.game_started = start == '1'
        self.unload_topic(topic_name)

        return self.game_started
    
    def play(self, selected_object, selected_object_parent):
        topic_guessing = open("./dialog_files/guessing.txt").read().format(object=selected_object, object_parent=selected_object_parent)
        topic_guessing_name = "play"
        self._loadTopic(topic_guessing_name, topic_guessing)

        correct = 0
        surrendered = 0

        while correct != '1' and surrendered != '1':
            correct = self.read_variable(nameof(correct))
            surrendered = self.read_variable(nameof(surrendered))

        self.unload_topic(topic_guessing_name)

    def play_again(self):
        topic_name = 'play_again'
        topic = open('./dialog_files/play_again.txt').read()
        
        self.load_topic(topic_name, topic)

        restarted = 0
        while restarted not in ['0', '1']:
            restarted = self.read_variable(nameof(restarted))
            time.sleep(1)

        self.unload_topic(topic_name)

        return restarted == '1'