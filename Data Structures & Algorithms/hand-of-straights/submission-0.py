class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        count = Counter(hand)
        # Sort the unique keys to always start forming groups from the smallest available card
        sorted_keys = sorted(count.keys())
        
        for key in sorted_keys:
            if count[key] > 0:
                start_count = count[key]
                # Check and consume the next groupSize consecutive cards
                for i in range(groupSize):
                    card = key + i
                    if count[card] < start_count:
                        return False
                    count[card] -= start_count
                    
        return True