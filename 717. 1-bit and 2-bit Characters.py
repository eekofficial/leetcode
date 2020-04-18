#https://leetcode.com/problems/1-bit-and-2-bit-characters/

class Solution:
    def isOneBitCharacter(self, bits) -> bool:
        current = ''
        currents = []
        for i in range(len(bits)):
            if current == '' and bits[i] == 0:
                current = ''
                currents.append(0)
            elif current == '' and bits[i] == 1:
                current = 1
            elif current == 1 and bits[i] == 1:
                current = ''
                currents.append(11)
            elif current == 1 and bits[i] == 0:
                current = ''
                currents.append(10)
        return currents[len(currents) - 1] == 0
                    
