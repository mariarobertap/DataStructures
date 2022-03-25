"https://leetcode.com/problems/remove-duplicates-from-sorted-array/"

def removeDuplicates(self, nums):
        
    k = 0

    for i in range(len(nums)):

        if nums[i] != nums[k]:
            k += 1
            nums[k] = nums[i]
            

    return k+1
        

numsAux = [0,0,1,1,1,1,1,1,2,2,2,3,3,4,4,4,4]
print(removeDuplicates(numsAux))
        