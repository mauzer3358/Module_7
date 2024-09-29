import re
class WordsFinder:
    def __init__(self, *file_names):
        self.filenames = file_names

    def get_all_words(self):
        self.all_words = {}
        self.split_words = []
        for f in self.filenames:
            self.name = f

        with open(self.name, 'r') as file:
            for lines in file:
                s1 = re.sub("[','| '.'| '='| '!'| '?'| ';'| ':'| ' - ']", " ", lines).split()
                for j in s1:
                    j = j.lower()
                    self.split_words.append(j)
        self.all_words[self.name] = self.split_words

        return self.all_words

    def find (self, word):
        self.word = word.lower()
        self.find_word = {}
        for word in self.get_all_words().values():
            print('word', word)
            self.to_find = word.index(self.word)
            self.find_word[self.name] = self.to_find
        return self.find_word

    def count(self, word):
        self.word = word.lower()
        self.count_word = {}
        self.count = 0
        for word in self.get_all_words().values():
            self.count = [i for i, x in enumerate(word) if x == self.word]
        self.count_word[self.name] = len(self.count)
        return self.count_word


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего