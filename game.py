"""Module docstring"""
import random
import string
import requests

class Game(): # pylint: disable=too-few-public-methods
    """docstring for Game"""
    def __init__(self):
        self.grid = []
        for _ in range(9):
            self.grid.append(random.choice(string.ascii_uppercase))
        print(self.grid)

    def is_valid(self, word):
        """docstring of is_valid method"""
        if not word:
            return False
        letters = self.grid[:]
        for letter in word:
            if letter in letters:
                letters.remove(letter)
            else:
                return False
        url = f"https://wagon-dictionary.herokuapp.com/{word}"
        r = requests.get(url)
        return r.json()["found"]


if __name__ == '__main__':
    Game()
