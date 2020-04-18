# https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, S: str):
        labels = []
        if len(S) == 0:
            return [0]
        left_s = ''
        i = 0
        while i < len(S):
            elem = S[i]
            left_s += elem
            j = i + 1
            last_pos = i
            while j < len(S):
                if S[j] in left_s:
                    left_s = S[i:j + 1]
                    last_pos = j   
                j += 1
            labels.append(len(left_s))
            left_s = ''
            i = last_pos + 1
        return labels
                
            
