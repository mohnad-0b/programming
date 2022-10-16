class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        valid =[]
        for i in range(len(points)):
            if x == points[i][0] or y == points[i][1]:
                valid.append(i)
        valid_point = []

        for i in valid :
            valid_point.append([(abs(x - points[i][0]) + abs(y - points[i][1])),i])
        valid_point = sorted(valid_point, key = lambda x: (x[0], x[1]))
        if (valid_point) :
            return (valid_point)[0][1]
        else:
            return -1