import pyperclip
import time
from urllib import parse , request

tmp = ""
if pyperclip.paste().__eq__('__break__'):pyperclip.copy("__restart__")
user_email = "434835764@qq.com"
while True:
    if tmp.__eq__('__break__') or tmp.__eq__("__break__"): break;
    if tmp != pyperclip.paste():
        print (pyperclip.paste())
        tmp = pyperclip.paste()
        url_encode = parse.quote(tmp)
        try:
            url = "http://www.nashuju.com:8082/index/visit/"+user_email+"/"+ url_encode
            response = request.urlopen(url)
        except:
            continue
        time.sleep(1)