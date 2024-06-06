class MinMaxWordFinder:
    def __init__(self):
        self.shortest_words = []
        self.longest_words = []
        self.word_length_map = {}  # Словарь для хранения слов по их длине

    def add_sentence(self, sentence):
        words = sentence.split()
        for word in words:
            word_length = len(word)
            if word_length not in self.word_length_map:
                self.word_length_map[word_length] = set()
            self.word_length_map[word_length].add(word)
            if not self.shortest_words or word_length < len(self.shortest_words[0]):
                self.shortest_words = [word]
            elif word_length == len(self.shortest_words[0]):
                self.shortest_words.append(word)
            if not self.longest_words or word_length > len(self.longest_words[0]):
                self.longest_words = [word]
            elif word_length == len(self.longest_words[0]):
                if word not in self.longest_words:
                    self.longest_words.append(word)

        self.shortest_words.sort()
        self.longest_words.sort()

    def shortest(self):
        return self.shortest_words

    def longest(self):
        return self.longest_words


finder = MinMaxWordFinder()
finder.add_sentence('hello')
finder.add_sentence(' abc def ')
finder.add_sentence('world')
finder.add_sentence(' abc ')
finder.add_sentence('asdf')
finder.add_sentence('qwert')

print(''.join( finder.shortest()))  
print(''.join(finder.longest()))    
