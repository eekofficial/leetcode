#https://leetcode.com/problems/find-smallest-letter-greater-than-target/

class Solution:
    def nextGreatestLetter(self, letters, target: str) -> str:
        index = bisect.bisect(letters, target)
        return letters[index % len(letters)]
