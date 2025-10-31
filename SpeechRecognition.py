#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 25 20:59:02 2025

@author: aakash-tiwari
"""

import speech_recognition as sr
AUDIO_FILE=("audio.wav")

# use the audio file as the source

r = sr.Recognizer() # initialize the recognizer

with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)
    # read the audio file
    
try:
    print("audio file contains", r.recognize_google(audio))
except  sr.UnknownValueError:
    print("Google Speech Recognition couldn't understand audio")
except sr.RequestError:
    print("Couldn't get the result from google speech recognition")