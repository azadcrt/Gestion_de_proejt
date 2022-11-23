#!/usr/bin/env python3                                                                                

import speech_recognition as sr
r = sr.Recognizer()

hellow=sr.AudioFile('stop.wav')
with hellow as source:
    audio = r.record(source)
try:
    s = r.recognize_google(audio)
    print(s)
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Could not request results")

