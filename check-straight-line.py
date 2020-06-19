'''
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point.
Check if these points make a straight line in the XY plane.

Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true

Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false
'''

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) == 1 or len(coordinates) == 2:
            return True

        # separate all coordinated
        x = [c[0] for c in coordinates] # O(N)
        y = [c[1] for c in coordinates] # O(N)

        # get the pattern of diffs for each axis
        x_patt, y_patt = self.get_pattern(x,y) # O(N)

        # calculate the slope (y1 - y / x1 - x)
        try:
            slope = y_patt[0] / x_patt[0]
        except ZeroDivisionError:
            return False

        # iterate through both one list, checking if slope matches by using index for other list
        for (i, x_diff) in enumerate(x_patt[1:]): # O(N)
            try:
                if y_patt[1:][i] / x_diff != slope:
                    return False
            except ZeroDivisionError:
                return False

        return True

    def get_pattern(self, x, y):
        x_patt = []
        y_patt = []
        # for each number in the x list
        for (i,cx) in enumerate(x):
            # if we're not at the second to last element
            if i+1 < len(x):
                # get the diff (next number - current number)
                x_diff = abs(x[i+1] - x[i])
                # use index to access y list
                y_diff = abs(y[i+1] - y[i])
                # add to pattern lists
                x_patt.append(x_diff)
                y_patt.append(y_diff)

        return x_patt, y_patt
