class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)):
            value = nums[i]
            if value in nums[i+1:]:
                return True
        return False

        