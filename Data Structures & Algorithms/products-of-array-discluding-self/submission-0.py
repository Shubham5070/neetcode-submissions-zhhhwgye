class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left=[]
        right=[0]*len(nums)
        x=1
        for i in range(len(nums)):
            left.append(x)
            x*=nums[i]
        print(left)
        
        y = 1
        for j in range(len(nums)-1, -1, -1):
            right[j] = y   # ✅ fix: assign correct index
            y *= nums[j]
        print(right)

        res = []
        for k in range(len(nums)):
            res.append(right[k] * left[k])
        print(res)
        return res
        


