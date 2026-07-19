import heapq
from collections import defaultdict

class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)      # userId -> [(time, tweetId)]
        self.following = defaultdict(set)    # userId -> set of followees

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int):
        maxHeap = []

        # include self + followees
        users = self.following[userId] | {userId}

        # load heap with most recent tweet from each user
        for u in users:
            if self.tweets[u]:
                idx = len(self.tweets[u]) - 1
                time, tweetId = self.tweets[u][idx]
                heapq.heappush(maxHeap, (-time, tweetId, u, idx))

        res = []

        # merge streams
        while maxHeap and len(res) < 10:
            negTime, tweetId, u, idx = heapq.heappop(maxHeap)
            res.append(tweetId)

            # push next older tweet from same user
            if idx - 1 >= 0:
                time, tweetId = self.tweets[u][idx - 1]
                heapq.heappush(maxHeap, (-time, tweetId, u, idx - 1))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)