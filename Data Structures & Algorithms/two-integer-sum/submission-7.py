class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i, n in enumerate(nums):
            # i = index
            # n = number
            hash_map[n] = i
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hash_map and hash_map[diff] != i:
                return [i, hash_map[diff]]
        return []

