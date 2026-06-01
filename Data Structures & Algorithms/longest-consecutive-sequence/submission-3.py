class Solution:
    def longestConsecutive(self, nums):
        x = set(nums)
        maxcount = 0

        for i in range(len(nums)):
            if nums[i] - 1 in x:
                continue
            else:
                count = 1
                curr = nums[i]

                while curr + 1 in x:
                    curr += 1
                    count += 1

                maxcount = max(maxcount, count)

        return maxcount