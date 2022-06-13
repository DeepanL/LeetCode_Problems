# 1232. Check If It Is a Straight Line

'''
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

Example 1:

Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true

Example 2:

Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false

Constraints:

    2 <= coordinates.length <= 1000
    coordinates[i].length == 2
    -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
    coordinates contains no duplicate point.


'''
import numpy as np
# Hint1: If there're only 2 points, return true.
# Hint2: Check if all other points lie on the line defined by the first 2 points.
# Hint3: Use cross product to check collinearity.

class Solution:
    def checkStraightLine(self, coordinates: list[list[int]]) -> bool:
        def slope(point1, point2):
            if (point2[0] - point1[0]) == 0:
                return None
            return ((point2[1] - point1[1])/(point2[0] - point1[0]))
        if len(coordinates) == 2:
            return True
        first_1 = coordinates[0]
        first_2 = coordinates[1]
        first_slope = slope(first_1,first_2)

        for i in range(1,len(coordinates)-1):
            pts_1 = coordinates[i]
            pts_2 = coordinates[i+1]
            check_slope = slope(pts_1,pts_2)
            if check_slope != first_slope:
                return False

        return True
        
        
        if len(coordinates) == 2:
            return True
        check_slope = slope(coordinates[0], coordinates[1])
        # print(coordinates[0])
        # print(coordinates[1])
        print(check_slope)
        # for i in range(1,len(coordinates)-1):
        #     # print(i)
        #     # print(slope(coordinates[i], coordinates[i+1]))
        #     if slope(coordinates[i], coordinates[i+1]) != check_slope:
        #         return False
        return True





# sol = Solution()
# sol.checkStraightLine(None).slope(None,None)
print(Solution().checkStraightLine([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]))
print(Solution().checkStraightLine([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]))

print(Solution().checkStraightLine([[0,0],[0,1],[0,-1]]))
print(Solution().checkStraightLine([[1,-8],[2,-3],[1,2]]))