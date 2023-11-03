"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    def __init__(self):
        self.word_lst = self.get_word_lst()

    def get_word_lst(self):
        """
        Returns a list of words read from the 'words.txt' file.

        >>> wf = WordFinder()
        >>> len(wf.get_word_lst())
        235886
        >>> wf.get_word_lst()[0]
        'A\n'
        >>> wf.get_word_lst()[-1]
        'Zyzzogeton\n'
        """
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
        """
        Returns a random word from the word list.

        >>> wf = WordFinder()
        >>> isinstance(wf.get_rand_word(), str)
        True
        >>> wf.get_rand_word() in wf.word_lst
        True
        """
        random_index = random.randrange(len(self.word_lst))
        random_word = self.word_lst[random_index].rstrip('\n')
        return random_word

class SpecialWordFinder(WordFinder):
    def __init__(self):
        super().__init__()

    def get_word_lst(self):
        word_lst = super().get_word_lst()
        word_lst = [word for word in word_lst if not word.startswith('#') and word.strip()]
        return word_lst

