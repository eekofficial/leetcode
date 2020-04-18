# https://leetcode.com/problems/flood-fill/

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        old_color = image[sr][sc]
        if old_color != newColor:
            self.flood_fill(image, sr, sc, old_color, newColor)
        return image
        
    def flood_fill(self, image, sr, sc, old_color, new_color):
            image[sr][sc] = new_color
            for dx, dy in ((+1, 0), (-1, 0), (0, +1), (0, -1)):
                x, y = sr + dx, sc + dy
                if 0 <= x < len(image) and 0 <= y < len(image[0]) and image[x][y] == old_color:
                    self.flood_fill(image, x, y, old_color, new_color)
        
