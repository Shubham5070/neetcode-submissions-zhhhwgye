class Solution:
    def topKFrequent(self, nums, k):

        x = {}

        for num in nums:
            if num in x:
                x[num] += 1
            else:
                x[num] = 1

        bucket = [[] for _ in range(len(nums) + 1)]

        for num, freq in x.items():
            bucket[freq].append(num)

        m = []

        for i in range(len(bucket)-1, 0, -1):

            if bucket[i]:

                for num in bucket[i]:

                    m.append(num)

                    if len(m) == k:
                        return m