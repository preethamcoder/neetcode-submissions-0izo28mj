class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        left = 0
        res = 0
        right = len(people)-1
        people.sort()
        while left <= right:
            total = people[left]+people[right]
            if total > limit:
                right -= 1
            else:
                left += 1
                right -= 1
            res += 1
        return res