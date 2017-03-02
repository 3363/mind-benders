import urllib
def check_word(text_to_check):
    url = "http://www.wdylike.appspot.com/?q=" + text_to_check
    params = urllib.urlencode({text_to_check: 0})
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=%s" % params)

    output = connection.read()
    print output
    connection.close()

def read_text():
    quotes = open("/home/argon/Documents/read_me.txt")
    file_text = quotes.read()
    print file_text
    quotes.close()
    check_word(file_text)


read_text()


