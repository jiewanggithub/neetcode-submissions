class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list) # userId -> list of [count, tweetId]
        self.followeeMap = defaultdict(set) # userId -> followee Id
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1 

    def getNewsFeed(self, userId: int) -> List[int]:
        minHeap = []
        res = []
        self.followeeMap[userId].add(userId)
        for Id in self.followeeMap[userId]:
            if Id in self.tweetMap:
                index = len(self.tweetMap[Id]) - 1
                count, tweetId = self.tweetMap[Id][-1]
                minHeap.append([count, tweetId, Id, index - 1])
        heapq.heapify(minHeap)

        while len(minHeap) and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:    
        self.followeeMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followeeMap[followerId]:
            self.followeeMap[followerId].remove(followeeId)
