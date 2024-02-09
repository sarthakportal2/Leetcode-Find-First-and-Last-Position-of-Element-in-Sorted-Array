class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        f1,l1=-1,-1#first and last variables declaration
        for i in range(len(nums)):#nums arr itration
            if nums[i]==target:# checking both Target arr eq 
                if f1==-1:f1=i#first var checking and assigning to it s arr's indx pos
                l1=i#last indx pos declaration
        
        return [f1,l1]#printing both the indx values
        
