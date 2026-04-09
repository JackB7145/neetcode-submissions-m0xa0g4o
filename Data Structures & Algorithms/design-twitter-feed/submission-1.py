class Twitter:

    def __init__(self):
        self.posts = []
        self.followList = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        heapq.heappush(self.posts, (-len(self.posts), userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        temp = []
        res = []
        print(self.posts, userId)
        while len(res) <= 9 and self.posts:
            node = heapq.heappop(self.posts)
            if (node[1] in self.followList[userId] or node[1] == userId):
                res.append(node[2])
            temp.append(node)
        while temp:
            heapq.heappush(self.posts, temp.pop())

        return res
            

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followList[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followList[followerId].remove(followeeId)
