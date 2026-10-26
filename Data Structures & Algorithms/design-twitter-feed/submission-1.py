import collections
import heapq

class Twitter:

    def __init__(self):
        self.time = 0
        self.followMap = collections.defaultdict(set)        
        self.tweets = collections.defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        allTweets = []

        self.followMap[userId].add(userId)

        for followee in self.followMap[userId]:
            if followee in self.tweets:
                for time, tweetId in self.tweets[followee]:
                    allTweets.append((time, tweetId))
        allTweets.sort()
        return [tweetId for time, tweetId in allTweets[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
