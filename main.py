# Tianze Created this code in 9/30/2024
import json
import pyaudio
import numpy as np
from vosk import Model, KaldiRecognizer, SetLogLevel
import threading


class Recorder:
    def __init__(self, model):
        self.model = model
        self.is_recording = False
        self.audio = pyaudio.PyAudio()
        self.stream = None

    def start_recording(self):
        self.is_recording = True
        self.stream = self.audio.open(format=pyaudio.paInt16,
                                      channels=1,
                                      rate=44100,
                                      input=True,
                                      frames_per_buffer=4000)
        self.frames = []
        self.thread = threading.Thread(target=self.record)
        self.thread.start()

    def record(self):
        print("开始录音...")
        count = 0
        THRESHOLDNUM = 30
        THRESHOLD = 100

        while self.is_recording and count < THRESHOLDNUM:
            data = self.stream.read(4000, exception_on_overflow=False)
            np_data = np.frombuffer(data, dtype=np.int16)
            frame_energy = np.mean(np.abs(np_data))
            if frame_energy < THRESHOLD:
                count += 1
            else:
                count = 0

            self.frames.append(data)

        print("停止录音!")
        self.stream.stop_stream()
        self.stream.close()
        self.audio.terminate()

    def stop_recording(self):
        self.is_recording = False
        self.thread.join()

    def get_transcription(self):
        rec = KaldiRecognizer(self.model, 44100)
        rec.SetWords(True)
        str_ret = ""
        for data in self.frames:
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                if 'text' in result:
                    str_ret += result['text']

        result = json.loads(rec.FinalResult())
        if 'text' in result:
            str_ret += result['text']

        str_ret = "".join(str_ret.split())
        return str_ret


if __name__ == "__main__":
    model = Model("vosk-model-cn-0.15")
    SetLogLevel(-1)

    recorder = Recorder(model)

    input("按下回车键开始录音...")
    recorder.start_recording()

    input("按下回车键停止录音...")
    recorder.stop_recording()

    transcription = recorder.get_transcription()
    if transcription:
        print(transcription)
