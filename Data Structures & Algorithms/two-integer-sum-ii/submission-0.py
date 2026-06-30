class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """hash_map = defaultdict(int) 
        for i in range(len(numbers)):
            tmp = target - numbers[i]
            if hash_map[tmp]:
                return [[hash_map[tmp], i+1]]
            hash_map[numbers[i]] = i + 1
        return []"""

        # two pointer solution
        l = 0
        r = len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]
            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l+1, r+1]
        return [[]]
    