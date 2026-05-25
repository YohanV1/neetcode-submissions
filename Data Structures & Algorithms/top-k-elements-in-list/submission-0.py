from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = Counter(nums)
        l = sorted(dic, key=lambda f: dic[f])
        return l[-k:]

        