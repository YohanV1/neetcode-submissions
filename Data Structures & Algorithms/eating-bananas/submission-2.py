class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        hi = max(piles)
        lo = 1

        while lo <= hi:
            speed = (lo + hi)//2
            hours = 0

            for pile in piles:
                hours += math.ceil(pile/speed)
            
            if hours <= h:
                hi = speed - 1
            else:
                lo = speed + 1
        return lo