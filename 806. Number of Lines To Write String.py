#https://leetcode.com/problems/number-of-lines-to-write-string/

class Solution:
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        if len(S) > 0:
            strings = 1
        else:
            return [0, 0]
        current_on_string = 0
        for letter in S:
            current_width = widths[ord(letter) - ord('a')]
            if current_on_string + current_width <= 100:
                current_on_string += current_width
            else:
                strings += 1
                current_on_string = current_width
        return [strings, current_on_string]
            
