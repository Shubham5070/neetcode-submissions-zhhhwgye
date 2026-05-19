class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        x={}
        for num in nums:
            if num in x:
                x[num]+=1
            else:
                x[num]=1
        print(x)
        xm=sorted(x.items(),key=lambda x:x[1],reverse=True)
        print(xm) 
        m=[]
        for i in range(k):
            m.append(xm[i][0])
        return m
