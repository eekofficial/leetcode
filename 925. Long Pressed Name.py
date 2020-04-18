#https://leetcode.com/problems/long-pressed-name/

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if len(name) == 0 or len(typed) < len(name):
            return False
        
        name_ind = 0
        typed_ind = 0
        while name_ind < len(name) and typed_ind < len(typed):
            if name[name_ind] == typed[typed_ind]:
                letter = name[name_ind]
                count_name = 1
                count_typed = 1
                while typed_ind < len(typed) and typed[typed_ind] == letter:
                    if typed_ind + 1 < len(typed):
                        typed_ind += 1
                        if typed[typed_ind] == letter:
                            count_typed += 1
                    else:
                        typed_ind += 1
                while name_ind < len(name) and name[name_ind] == letter:
                    if name_ind + 1 < len(name):
                        name_ind += 1
                        if name[name_ind] == letter:
                            count_name += 1
                    else:
                        name_ind += 1
                if count_typed < count_name:
                    return False
            else:
                return False
        if name_ind < len(name):
            return False
        return True
