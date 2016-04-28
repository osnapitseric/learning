import urllib
import random
import urllib.request

class name(object):
    def __init__(self, name):
        self.name = name

    def wbank(self):
        words = []
        wordurl = "http://learncodethehardway.org/words.txt"
        for i in urllib.request.urlopen(wordurl).readlines():
            words.append(i.strip())
        print(words)

    def randommath(self):
        random.randint(0, 1000000000)

x = name("eric")
x.wbank()
