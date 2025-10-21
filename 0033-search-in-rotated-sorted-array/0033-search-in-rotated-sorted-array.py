class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums: return -1
        # almost standard bs
        l, r = 0, len(nums)-1
        while l<r:
            m = (l+r)//2
            if target == nums[m]: return m
            # is the left sorted?
            if nums[l] < nums[m]:
                if nums[l] <= target <= nums[m]: r = m
                else: l = m+1
            # then right is sorted...
            else: 
                if nums[m+1] <= target <= nums[r]: l = m+1
                else: r = m
        return l if nums[l] == target else -1