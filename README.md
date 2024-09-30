# Speech-to-Text
# Overview
This is a tool for audio recording and transcription using the Vosk speech recognition library, written in Python.It enables recording audio via the microphone, and subsequently transcribing the audio into text using a specified Vosk model.
# Features
- **Real-time audio recording:** Capture audio input from the microphone.
- **Voice activity detection (VAD):** Automatically stops recording when the sound falls below a certain threshold for a set duration.
- **Speech transcription:** Converts recorded audio into text using the Vosk speech recognition engine.
# Requirements
## Dependencies
To run this program, the following Python packages must be installed:
- pyaudio - For audio input.
- vosk - For speech recognition and transcription.
- numpy - For numerical processing of audio frames.
## Installation
Use pip to install the required dependencies:
- pip install pyaudio vosk numpy
## Additional Files
Download the Vosk model for speech recognition.Please go to this cloud storage website to get it:https://pan.baidu.com/s/1UUaPZ4l-xPLOuyJU9tmdXw Pin:6666   
# Usage
- Clone the repository or download the script.
- Ensure you have installed the required dependencies and the Vosk model.
- Run the code.
- Follow the prompts to start and stop recording:<br>1.Press Enter to start recording.<br>2.Press Enter again to stop the recording.<br>
- Once the recording is stopped, the audio will be transcribed, and the text will be printed to the console.
# Configuration
The following parameters can be adjusted for better performance:
- THRESHOLD: Controls the voice activity detection sensitivity. Lower values make the recorder more sensitive to quieter sounds.
- THRESHOLDNUM: Sets how many frames must pass the threshold before stopping the recording.
# Acknowledgements
- Vosk API for the speech recognition engine.
- PyAudio for handling the audio input.
