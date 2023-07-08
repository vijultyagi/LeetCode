# O(1) Space Complexity
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)

        #Reverse whole array
        nums.reverse()

        #Reverse first k elements
        for i in range(k//2):
            nums[i], nums[k-1-i] = nums[k-1-i], nums[i]

        #Reverse rest of the elements
        for j in range(k, (len(nums)+k)//2):
            nums[j], nums[len(nums)-1-j+k] = nums[len(nums)-1-j+k], nums[j]
        
        return nums