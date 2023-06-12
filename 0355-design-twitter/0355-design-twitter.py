class Twitter:

    def __init__(self):
        self.max_heap = []
        self.followLink = defaultdict(set)
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        heapq.heappush(self.max_heap, (-len(self.max_heap), tweetId, userId))

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        temp = []
        while self.max_heap and len(res)!= 10:
            idx, tw, us = heapq.heappop(self.max_heap)
            if us in self.followLink[userId] or us == userId:
                res.append((-idx, tw, us))
            else:
                temp.append((-idx, tw, us))
        t = []
        for i in res:
            heapq.heappush(self.max_heap, (-i[0], i[1], i[2]))
            t.append(i[1])
        for i in temp:
            heapq.heappush(self.max_heap, (-i[0], i[1], i[2]))
        return t
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followLink[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followLink[followerId]:
            self.followLink[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)