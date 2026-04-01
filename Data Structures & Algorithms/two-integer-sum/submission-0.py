class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}  # value -> index
        
        for i in range(len(nums)):
            complement = target - nums[i]
            
            # check if complement already seen
            if complement in hashmap:
                return [hashmap[complement], i]
            
            # store current number
            hashmap[nums[i]] = i