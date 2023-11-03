"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    def __init__(self):
        self.word_lst = self.get_word_lst()

    def get_word_lst(self):
        word_lst = []
        word_count = 0
        file = open('words.txt', 'r')
        for line in file:
            word_lst.append(line)
            word_count +=1
        file.close()
        print(f'{word_count} words read')
        return word_lst

    def get_rand_word(self):
        random_index = random.randrange(len(self.word_lst))
        random_word = self.word_lst[random_index].rstrip('\n')
        return random_word


