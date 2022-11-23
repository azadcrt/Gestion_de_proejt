#!/usr/bin/env python3                                                                                

import speech_recognition as sr  

# get audio from the microphone                                                                       
r = sr.Recognizer() 

print(sr.Microphone.list_microphone_names())                                                                                  
with sr.Microphone(device_index=2) as source:                                                                       
    print("Speak:")  
    print(sr.Microphone(device_index=2))    
    print(source)                                                            
    audio = r.listen(source)   

try:
    print("You said " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))
