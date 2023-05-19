class Solution:
    def majorityElement(self, A, N):
        #Your code here
        dic={}
        found=0
        for x in A:
            if x not in dic:
                dic[x]=1
                if dic[x]>N/2:
                    found+=1
                    break
            else:
                dic[x]=dic[x]+1
                if dic[x]>N/2:
                    found+=1
                    break
        if found==0:
            return -1
        else:
            return x
