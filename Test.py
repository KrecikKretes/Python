import speech_recognition as sr
r = sr.Recognizer()
mic = sr.Microphone(device_index=0)
while 1:
    with mic as source:
        audio = r.listen(source)
    x=r.recognize_google(audio)
    if x=="computer" :
        print("Yes")


