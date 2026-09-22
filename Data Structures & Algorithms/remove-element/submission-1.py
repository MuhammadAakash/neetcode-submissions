class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0;
        for num in range(len(nums)):
            if nums[num] != val:
                nums[k] = nums[num]
                k += 1
                
        
        print("K is this", k, "Nums is this :", nums)
        return k