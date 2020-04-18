#https://leetcode.com/problems/day-of-the-year/

class Solution:
    def dayOfYear(self, date: str) -> int:
        usual = {1:0, 2:31, 3:59, 4:90, 5:120, 6:151, 7:181, 8:212, 9:243, 10:273, 11:304, 12:334}
        bis_sextus = {1:0, 2:31, 3:60, 4:91, 5:121, 6:152, 7:182, 8:213, 9:244, 10:274, 11:305, 12:335}
        date = date.split('-')
        if int(date[0]) % 400 == 0:
            return bis_sextus[int(date[1])] + int(date[2])
        elif int(date[0]) % 100 == 0:
            return usual[int(date[1])] + int(date[2])
        elif int(date[0]) % 4 == 0:
            return bis_sextus[int(date[1])] + int(date[2])
        else:
            return usual[int(date[1])] + int(date[2])
        
