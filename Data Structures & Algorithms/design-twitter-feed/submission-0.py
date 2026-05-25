from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.timestamp = 0
        self.tweets = defaultdict(list)     # userId -> list of (timestamp, tweetId)
        self.following = defaultdict(set)   # userId -> set of users they follow

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Store tweet with timestamp (negative for max-heap)
        self.tweets[userId].append((-self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        maxHeap = []

        # Everyone follows themselves
        self.following[userId].add(userId)

        # Push the most recent tweet from each followee
        for followee in self.following[userId]:
            if self.tweets[followee]:
                time, tid = self.tweets[followee][-1]
                idx = len(self.tweets[followee]) - 1
                heapq.heappush(maxHeap, (time, tid, followee, idx - 1))

        result = []
        while maxHeap and len(result) < 10:
            time, tid, uid, idx = heapq.heappop(maxHeap)
            result.append(tid)

            # Push the next older tweet from the same user
            if idx >= 0:
                time2, tid2 = self.tweets[uid][idx]
                heapq.heappush(maxHeap, (time2, tid2, uid, idx - 1))

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:  # cannot follow yourself
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
