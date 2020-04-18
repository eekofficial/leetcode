#https://leetcode.com/problems/image-smoother/

class Solution:
    def imageSmoother(self, M):
        smoother = []
        for i in range(len(M)):
            smoother.append([])
            for j in range(len(M[0])):
                smoother[i].append(0)
        
        for i in range(len(M)):
            for j in range(len(M[0])):
                sum_of_color = 0
                count = 0
                for dx, dy in ((0, 0), (+1, 0), (-1, 0), (0, +1), (0, -1), (-1, -1), (+1, +1), (-1, +1), (+1, -1)):
                    x = i + dx
                    y = j + dy
                    if 0 <= x < len(M) and 0 <= y < len(M[0]):
                        count += 1
                        sum_of_color += M[x][y]
                smoother[i][j] = math.floor((sum_of_color / count))
        return smoother
