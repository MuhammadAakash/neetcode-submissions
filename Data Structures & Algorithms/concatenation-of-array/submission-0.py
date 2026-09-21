class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        new_array_length = 2 * len(nums)
        ans = [0] * new_array_length

        for i in range(len(nums)):
            ans[i] = nums[i]
        
        for i in range(len(nums) , 2 * len(nums)):
            ans[i] = nums[i - len(nums)]

        print(ans)
        return ans