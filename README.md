# Voice-conversion
# Overview
The Recorder class is a Python implementation of an audio recording and transcription tool using the Vosk speech recognition library. It enables recording audio via the microphone, and subsequently transcribing the audio into text using a specified Vosk model.
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
  
