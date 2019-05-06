class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        nrow = len(image)
        if nrow == 0: return image
        ncol = len(image[0])

        queue = [(sr, sc)]

        oldColor = image[sr][sc]
        # edge case: when newColor is same, avoid infinite loop
        if newColor == oldColor:
            return image
        image[sr][sc] = newColor

        inBound = lambda r, c: 0 <= r and r < nrow and 0 <= c and c < ncol

        while queue:
            r, c = queue.pop(0) # pop left
            for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                rr, cc = r + dr, c + dc

                # if position is valid, replace color and append to queue
                if inBound(rr, cc) and image[rr][cc] == oldColor:
                    image[rr][cc] = newColor
                    queue.append((rr, cc))

        return image
