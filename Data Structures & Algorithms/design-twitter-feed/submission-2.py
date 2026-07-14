class Twitter:

    def __init__(self):
        self.count  =0
        self.tweets = collections.defaultdict(list)
        self.followMap = collections.defaultdict(set)


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count -= 1
        self.tweets[userId].append([self.count, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []
        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweets:
                index = len(self.tweets[followeeId]) -1
                count, tweetId = self.tweets[followeeId][index]
                minHeap.append([count, tweetId, followeeId, index-1])
        heapq.heapify(minHeap)
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, idx = heapq.heappop(minHeap)
            res.append(tweetId)
            if idx >= 0:
                next_count, next_tweetId = self.tweets[followeeId][idx]
                heapq.heappush(minHeap,[next_count, next_tweetId, followeeId, idx -1])
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        
