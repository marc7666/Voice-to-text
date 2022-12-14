"""
__author__ = Marc Cervera Rosell
__company__ = Electrònica Saltó S.L.
__date__ = 14/12/2022
"""

import speech_recognition as sr


class SpeechRecognizer:
    """
    This class performs the task of recognizing the speech from a .wav audio file
    using a supported API from the speech_recognition library.
    """
    recognizer = None
    audio_file = None

    def __init__(self, audio_file):
        """
        Constructor of the class
        :param audio_file: Audio file from which the speech will be extracted
        """
        self.recognizer = sr.Recognizer()
        self.audio_file = audio_file

    def capture_audio_data(self):
        """
        This method, opens the audio file and records the data from the entire audio file,
        and saves it into an AudioData instance.
        If, for some reason, there's any error, an CaptureAudioDataException will be raised
        jointly with an error message.
        :return: Audio data
        """
        try:
            audio = sr.AudioFile(self.audio_file)
            with audio as source:
                audio_data = self.recognizer.record(source)
            return audio_data
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            raise

    def recognize(self, audio_data):
        """
        This method receives the recorded data of the audio file and transcripts them.
        If, for some reason, there's an error, a RecognizeException is raised jointly
        with an error message.
        :param audio_data: Recorded data of the audio file
        :return: None
        """
        try:
            self.recognizer.recognize_google(audio_data)
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            raise


if __name__ == "__main__":
    r = SpeechRecognizer("audio_file.wav")
    data = r.capture_audio_data()
    r.recognize(data)
