# -*- coding: utf-8 -*-
import pyaudio,os
import speech_recognition as sr
import platform
import subprocess
import sys
import os
import time
import PySimpleGUI as sg
from win32com.client import Dispatch


def mainfunction(source):
        
        if event == "STOP":
            exit()
        else:   
            speak = Dispatch("SAPI.SpVoice").Speak
            print("What?")
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            try:
                user = r.recognize_google(audio, language='pl-PL')
                print (user)
                if (user == "komputer"):
                    speak("Code?")
                    r.adjust_for_ambient_noise(source)
                    audio = r.listen(source)
                    try:
                        user = r.recognize_google(audio, language='pl-PL')
                        print (user)
                        if user == "10" or user =="dziesięć":
                            os.system("shutdown /h")
                        exit()
                        if user == "1" or user =="jeden":
                            os.system("notepad.exe")
                        if user == "0" or user =="zero":
                            exit()
                    except sr.UnknownValueError:
                        print ("None")
            except sr.UnknownValueError:
                    print ("None")
            time.sleep(5)
            mainfunction(source)

if __name__ == "__main__":
    layout = [[sg.Text("Hello")], [sg.Button("OK")],[sg.Button("STOP")]]
    window = sg.Window("Demo", layout)
    r = sr.Recognizer()
    with sr.Microphone() as source:
        event, values = window.read()
        mainfunction(source)
