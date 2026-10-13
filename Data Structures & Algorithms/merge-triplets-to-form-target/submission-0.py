class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        found = [False, False, False]
        
        for t in triplets:
            # If any value exceeds the target, this triplet is invalid
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            
            # Check which parts of the target this triplet can help form
            for i in range(3):
                if t[i] == target[i]:
                    found[i] = True
                    
        return all(found)