class Solution:
    def sortColors(self, nums: List[int]) -> None:
        #we can also do this using three pointers
        left = 0 
        right = len(nums) - 1
        i = 0 #current pointer 

        while i <= right:

            if nums[i] == 0:
                #swap with left 
                nums[i], nums[left] = nums[left], nums[i]
                left +=1
                i += 1 
            elif nums[i] == 2:
                nums[i], nums[right] = nums[right], nums[i]
                right -=1 
              
                
            
            else:
                i += 1
        

        
        