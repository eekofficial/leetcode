# https://leetcode.com/problems/bulls-and-cows/

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secret_dict = dict()
        guess_dict = dict()
        for i in range(len(secret)):
            secret_dict[i] = secret[i]
        for i in range(len(guess)):
            guess_dict[i] = guess[i]
        bulls = 0
        cows = 0
        looked = set()
        for position, digit in guess_dict.items():
            if secret_dict[position] == digit:
                bulls += 1
                secret_dict[position] = 'd'
                looked.add(position)
        secret_lost = []
        for digit in secret_dict.values():
            if digit != 'd':
                secret_lost.append(digit)
        for position, digit in guess_dict.items():
            if position not in looked:
                if digit in secret_lost:
                    cows += 1
                    secret_lost.pop(secret_lost.index(digit))
        return '{}A{}B'.format(bulls, cows)
                    
            
            
