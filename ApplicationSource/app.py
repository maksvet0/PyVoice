import re

import speech_recognition
import json



class Application:
    def __init__(self):
        self.sr = speech_recognition.Recognizer()
        self.app_conf_file = None
        self.speech_conf_file = None
        self.configure()
        self.sr.pause_threshold = self.speech_conf_file["pause_threshold_time"]

    def configure(self):
        with open('Res\\cofiguration\\speech.json') as speech_conf_file:
            self.speech_conf_file = json.load(speech_conf_file)
        with open('Res\\cofiguration\\app.json') as app_conf_file:
            self.app_conf_file = json.load(app_conf_file)
        with speech_recognition.Microphone() as mic:
            self.sr.adjust_for_ambient_noise(source=mic, duration=self.speech_conf_file["adaptation_duration"])

    def main(self):
        print(self.app_conf_file['h'])
        print(self.sr.pause_threshold)
        self.recognize()
        print('Exit please wait.....')
    def recognize(self):
        try:
            while True:
                with speech_recognition.Microphone() as mic:
                    self.sr.adjust_for_ambient_noise(source=mic, duration=self.speech_conf_file["adaptation_duration"])
                    query = self.sr.recognize_google(audio_data=self.sr.listen(source=mic), language='ru-RU').lower()
                if query != 'выход':
                    self.switch(query)
                else:
                    exit()
        except Exception as e:
            self.recognize()
    def switch(self, query):
        if re.search(r'\bpython\b', query):
            print(query)

if __name__ == '__main__':
    app = Application()
    app.main()
