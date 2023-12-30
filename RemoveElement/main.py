class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        r = nums.count(val)
        if not r:
            return len(nums)
        for i in range(r):
            for j in range(len(nums) - 1):
                if nums[j] == val:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return len(nums[:-r])
