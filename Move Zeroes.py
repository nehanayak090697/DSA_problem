class Solution:
    def moveZeroes(self, a: List[int]) -> None:
        i,j,temp=0,0,0
        n=len(a)
        while(j<n):
            if a[j]!=0 and temp==0:
                i+=1
                j+=1
            elif a[j]!=0 and temp==1:
                a[i],a[j]=a[j],a[i]
                i+=1
                j+=1
            elif a[j]==0 :
                j+=1
                temp=1
        
        
            
            
        
