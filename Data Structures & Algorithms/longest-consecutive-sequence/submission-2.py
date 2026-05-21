class Solution:
    def longestConsecutive(self, nums):

        x = set(nums)

        maxl = 0

        for num in x:

            # start of sequence
            if num - 1 not in x:

                current = num
                count = 1

                while current + 1 in x:

                    current += 1
                    count += 1

                maxl = max(maxl, count)

        return maxl