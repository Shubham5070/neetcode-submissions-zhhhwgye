class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        x=nums
        left=[1]
        right=[1]

        for i in range(0,len(x)):
            left.append(x[i]*left[-1])

        for j in range(len(x)-1,-1,-1):
            right.append(x[j]*right[-1])
        right.reverse()
            
        print(left,right)
        ans=[]

        for i in range(0,len(x)):
            ans.append(left[i]*right[i+1])
        return ans
                