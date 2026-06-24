class Solution:
    def removeElement(self, nums: List[int], k: int) -> int:
        while k in nums:
            nums.remove(k);

        return len(nums) 