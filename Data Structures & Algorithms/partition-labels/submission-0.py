class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = {char: i for i, char in enumerate(s)}
        
        res = []
        size = 0
        end = 0
        
        # Step 2: Iterate through the string and greedily extend partitions
        for i, char in enumerate(s):
            size += 1
            end = max(end, last_index[char])
            
            # If current index matches the furthest last index seen, we found a partition
            if i == end:
                res.append(size)
                size = 0
                
        return res