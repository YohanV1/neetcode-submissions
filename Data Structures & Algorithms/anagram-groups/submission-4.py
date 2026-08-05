class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)

        for st in strs:
            count = [0] * 26
            for letter in st:
                count[ord(letter) - ord('a')] += 1
            res[tuple(count)].append(st)
        return list(res.values())