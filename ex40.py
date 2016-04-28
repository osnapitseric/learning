"""
class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

    def comment(self, v):
        print("good job", v)

    def rename(self):
        self.sing_me_a_song()
        new_song = input("what's your song?: ")
        print(new_song)
        a = b

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there."])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

eric = Song("eric")


happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
print(happy_bday.lyrics)
happy_bday.rename()
"""

def wbank():
    words = []
    for file in open("/Users/eric/virtualenv/pyproject/list.txt", mode="r", encoding="utf-8").readlines():
        words.append(file.strip())
    print(words)

wbank()
