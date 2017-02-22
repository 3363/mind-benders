import webbrowser
import time

def openbrowser():
    i = 0
    while i < 3:        
        print time.ctime()
        time.sleep(5)
        print time.ctime()
        webbrowser.open("https://mail.zoho.com/zm/#mail/views/all")
        i += 1

openbrowser()
