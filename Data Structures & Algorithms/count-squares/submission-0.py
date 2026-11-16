class CountSquares:

    def __init__(self):
        self.ptsCount = {}  # Map from (x, y) to frequency
        self.pts = []       # List of all added points

    def add(self, point: List[int]) -> None:
        px, py = point[0], point[1]
        self.ptsCount[(px, py)] = self.ptsCount.get((px, py), 0) + 1
        self.pts.append(point)

    def count(self, point: List[int]) -> int:
        qx, qy = point[0], point[1]
        res = 0
        
        for x, y in self.pts:
            # Check if (x, y) forms a diagonal with (qx, qy)
            if abs(qx - x) != abs(qy - y) or x == qx or y == qy:
                continue
            
            # The other two corners must exist in our hash map
            corner1 = (x, qy)
            corner2 = (qx, y)
            
            if corner1 in self.ptsCount and corner2 in self.ptsCount:
                res += self.ptsCount[corner1] * self.ptsCount[corner2]
                
        return res
