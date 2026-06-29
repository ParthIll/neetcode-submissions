class Twitter:

    def __init__(self):
        self.following = {}
        self.time = 0
        self.feed={}
        self.posts={}
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time-=1
        if userId not in self.posts:
            self.posts[userId]=[]
        if userId not in self.feed:
            self.feed[userId]=[]
        if userId not in self.following:
            self.following[userId] = []
        self.posts[userId].append((self.time,userId,tweetId))
        self.feed[userId].append((self.time,userId,tweetId))
        for user in self.following[userId]:
            self.feed[user].append((self.time,userId,tweetId))
    def getNewsFeed(self, userId: int) -> List[int]:
        newsHeap =[]
        ret=[]
        for post in self.feed[userId]:
            heapq.heappush(newsHeap,post)
        newsHeap.sort()
        for post in newsHeap:
            ret.append(post[2])
        return ret[0:10]


    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.following:
            self.following[followeeId] =[]
        if followeeId not in self.posts:
            self.posts[followeeId] =[]
        if followerId not in self.feed:
            self.feed[followerId] = []
        if followerId != followeeId and followerId not in self.following[followeeId]:
            self.following[followeeId].append(followerId)
            for post in self.posts[followeeId]:
                self.feed[followerId].append(post)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.following:
            self.following[followeeId] =[]
        if followerId not in self.feed:
            self.feed[followerId]=[]
        if followerId != followeeId and followerId in self.following[followeeId]:
            self.following[followeeId].remove(followerId)
            removal = []
            for post in self.feed[followerId]:
                if post[1]==followeeId:
                    removal.append(post)
            for post in removal:
                self.feed[followerId].remove(post)