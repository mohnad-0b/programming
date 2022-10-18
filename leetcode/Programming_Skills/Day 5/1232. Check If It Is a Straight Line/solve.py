class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        
        try:
            m = abs(coordinates[0][0] - coordinates[-1][0])/abs(coordinates[0][1] - coordinates[-1][1])

            for i in  range(len(coordinates)-1) :

                if abs(coordinates[i][0] - coordinates[i+1][0])/abs(coordinates[i][1] - coordinates[i+1][1]) != m :            
                    return False
            return True
    
        except ZeroDivisionError:
            for i in range(len(coordinates)-1):
                if coordinates[i][1] != coordinates[i+1][1]:
                    return False
            return True