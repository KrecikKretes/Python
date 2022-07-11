# -*- coding: utf-8 -*-
import pyaudio,os
import speech_recognition as sr
import platform
import subprocess
import sys
import os
import soundmeter
import time



def mainfunction(source):
        print ("What?")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
             user = r.recognize_google(audio, language='pl-PL')
             print (user)
             if (user == "komputer"):
                print ("Code?")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
                try:
                        user = r.recognize_google(audio, language='pl-PL')
                        print (user)
                        if user == "10" or user =="ten":
                                os.system("shutdown /h")
                                exit()
                        if user == "1" or user =="one":
                                os.system("notepad.exe")
                        if user =="pisz":
                                subprocess.Popen(['C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE'])
                        if user == "film":
                                os.system('cd /d D:\\OBS\\obs-studio\\bin\\64bit')
                        #        os.system('start obs64.exe')
                        #      subprocess.Popen(['D:\\OBS\\obs-studio\\bin\\64bit\\obs64.exe'])
                        if user == "nauka":
                                os.system('start C:\\Users\\Krecik\\AppData\\Local\\Microsoft\\Teams\\Update.exe --processStart "Teams.exe"')

                        if user == "sen":
                                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
                except sr.UnknownValueError:
                    print ("None")
        except sr.UnknownValueError:
                print ("None")
        time.sleep(5)
        mainfunction(source)

if __name__ == "__main__":
    r = sr.Recognizer()
    with sr.Microphone() as source:
       mainfunction(source)
