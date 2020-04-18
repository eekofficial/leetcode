# 551. Student Attendance Record I

class Solution:
    def checkRecord(self, s: str) -> bool:
        a_count = 0
        l_count = 0
        i = 0
        while (a_count <= 1 and l_count <=2) and i < len(s):
            if s[i] == 'A':
                a_count += 1
                l_count = 0
            elif s[i] == 'L':
                l_count += 1
            else:
                l_count = 0
            i += 1
            if a_count > 1 or l_count > 2:
                return False
        return True
        
