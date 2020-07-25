#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 16:51:34 2020

@author: awakhiwekhabo
"""


import speech_recognition as sr

# initialize the recognizer
r = sr.Recognizer()

#prompt user to upload audio .wav file
ip = input("Upload your .wav audio file:")
filename = ip

# open the file
print("Processing...")
with sr.AudioFile(filename) as source:
    # listen for the data (load audio to memory)
    audio_data = r.record(source)
    # recognize (convert from speech to text)
    text = r.recognize_google(audio_data)
    print(text)
