import time
from image.imagegeneration import ImageGeneration
from exercises.file_transfer import FileTransfer

class Game():

    def __init__(self, robot, session_id):
        self.session_id = session_id
        self.robot = robot
        self._dialog_name = 'game_dialog'
        self.dialog = self.robot.session.service('ALDialog')
        self.memory = self.robot.session.service('ALMemory')
        self.dialog.openSession(self.session_id)
        self.textToSpeech = self.robot.session.service("ALTextToSpeech")
        self.textToSpeech.setLanguage("English")
        self.image_generation = ImageGeneration()
        self.local_folder_path = "C:\\Users\\timon\\Documents\\hslu\\06\\ROBO\\Pepper\\"
        self.remote_folder_path = "/opt/aldebaran/www/apps/"

        self._game_started = False
        self.reset()

    def __del__(self):
        for topic in self.dialog.getLoadedTopics('English'):
            self.unload_topic(topic)

        self.dialog.closeSession()

    def read_variable(self, name):
        return self.dialog.getUserData(name, self.session_id)

    def clear_variable(self, name):
        try:
            self.memory.removeData(name)
        except:
            pass
    
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

        start = None

        while start not in ['0', '1']:
            start = self.read_variable('start')
            time.sleep(1)

        self._game_started = start == '1'
        self.unload_topic(topic_name)

        return self._game_started
    
    def play(self, selected_object, selected_object_parent):
        if selected_object_parent is None:
            topic_guessing = open("./dialog_files/guessing_without_parent.txt").read()
        else:
            topic_guessing = open("./dialog_files/guessing.txt").read().format(object=selected_object,
                                                                               object_parent=selected_object_parent)
        topic_guessing_name = "play"
        self.load_topic(topic_guessing_name, topic_guessing)

        correct = 0
        surrendered = 0

        while correct != '1' and surrendered != '1':
            correct = self.read_variable("correct")
            surrendered = self.read_variable("surrendered")
            hint = self.read_variable("hint")
            if hint == '1':
                file_name = "hint.png"
                local_full_path = self.local_folder_path + file_name
                remote_full_path = self.remote_folder_path + file_name
                img_hint = self.image_generation.get_image_for_text(selected_object[0])
                img_hint.save(local_full_path)
                file_transfer = FileTransfer(self.robot)
                file_transfer.put(local_full_path, remote_full_path)
                file_transfer.close()
            time.sleep(1)

        self.unload_topic(topic_guessing_name)

    def play_again(self):
        self.reset()
        topic_name = 'play_again'
        topic = open('./dialog_files/play_again.txt').read()
        
        self.load_topic(topic_name, topic)

        restart = 0
        while restart not in ['0', '1']:
            restart = self.read_variable("restart")
            time.sleep(1)

        self.unload_topic(topic_name)

        return restart == '1'

    def reset(self):
        self.clear_variable("start")
        self.clear_variable("correct")
        self.clear_variable("surrendered")
        self.clear_variable("restart")
        self.clear_variable("hint")
        file_transfer = FileTransfer(self.robot)
        file_transfer.remove(self.remote_folder_path + 'hint.png')
        file_transfer.close()
