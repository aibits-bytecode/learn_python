class BubbleSort:

    def sort(self, nums):
        for i in range(len(nums)-1,0,-1):
            for j in range(i):
                if nums[j]>nums[j+1]:
                    nums[j] = nums[j] ^ nums[j+1]
                    nums[j+1] = nums[j] ^ nums[j + 1]
                    nums[j] = nums[j] ^ nums[j + 1]
        return nums


bs = BubbleSort()
nums = [1, 21, 52, 4, 26, 39]
print(bs.sort(nums))