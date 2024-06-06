class LeftParagraph:
    def __init__(self, width):
        self.width = width
        self.words = []
        self.current_line = ""

    def add_word(self, word):
        if len(self.current_line) + len(word) <= self.width:
            self.current_line += word + " "
        else:
            print(self.current_line.strip())
            self.current_line = word + " "

    def end(self):
        print(self.current_line.strip())
        print()


class RightParagraph:
    def __init__(self, width):
        self.width = width
        self.words = []
        self.current_line = ""

    def add_word(self, word):
        if len(self.current_line) + len(word) <= self.width:
            self.current_line = " " * (self.width - len(word)) + word + " "
        else:
            print(self.current_line.strip())
            self.current_line = " " * (self.width - len(word)) + word + " "

    def end(self):
        print(self.current_line.strip())
        print()


lp = LeftParagraph(8)
lp.add_word('abc')
lp.add_word('defg')
lp.add_word('hi')
lp.add_word('jklmnopq')
lp.add_word('r')
lp.add_word('stuv')
lp.end()

rp = RightParagraph(8)
rp.add_word('abc')
rp.add_word('defg')
rp.add_word('hi')
rp.add_word('jklmnopq')
rp.add_word('r')
rp.add_word('stuv')
rp.end()