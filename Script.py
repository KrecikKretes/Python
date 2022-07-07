import PIL.ImageGrab
import time
import win32com.client as comclt
wsh= comclt.Dispatch("WScript.Shell")
time.clock()
image = ImageGrab.grab()
for y in range(0, 100, 10):
    for x in range(0, 100, 10):
        color = image.getpixel((x, y))
        
        #wsh.AppActivate("D:\obs-studio\bin\64bit\obs64.exe")
        #wsh.SendKeys("a")
print(time.clock())