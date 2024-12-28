from typing import List

class Solution:
    def min_time_to_visit_all_points(self, points: List[List[int]]) -> int:
        res = 0
        for i in range(len(points) - 1):
            x1, y1 = points[i]
            x2, y2 = points[i + 1]
            res += max(abs(y2 - y1), abs(x2 - x1))
        return res
