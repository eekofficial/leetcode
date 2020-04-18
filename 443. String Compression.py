# https://leetcode.com/problems/string-compression/

class Solution:
    def compress(self, chars) -> int:
        if len(chars) == 0:
            return 0
        elem = chars[0]
        count_elem = 1
        last_not_repeated = 0
        for i in range(1, len(chars)):
            if chars[i] == elem:
                count_elem += 1
            else:
                if count_elem > 1:
                    chars[last_not_repeated] = elem
                    last_not_repeated += 1
                    count_elem = str(count_elem)
                    for j in range(len(count_elem)):
                        chars[last_not_repeated + j] = count_elem[j]
                    last_not_repeated += len(count_elem)
                else:
                    chars[last_not_repeated] = elem
                    last_not_repeated += 1
                elem = chars[i]
                count_elem = 1
        if count_elem > 1:
            chars[last_not_repeated] = elem
            last_not_repeated += 1
            count_elem = str(count_elem)
            for j in range(len(count_elem)):
                chars[last_not_repeated + j] = count_elem[j]
            last_not_repeated += len(count_elem)
        else:
            chars[last_not_repeated] = elem
            last_not_repeated += 1
        return last_not_repeated
