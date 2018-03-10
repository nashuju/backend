import pyperclip
import time


tmp = ""
while True:
    if tmp.__eq__('__break__') or tmp.__eq__("__break__"): break;
    if tmp != pyperclip.paste():
        print (pyperclip.paste())
        tmp = pyperclip.paste()
        time.sleep(1)