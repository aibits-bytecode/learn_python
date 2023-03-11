class SelectionSort:

    def sort(self, nums):
        for i in range(len(nums)-1):
            min = i
            for j in range(i, len(nums)):
                if nums[j] < nums[min]:
                    min = j
            if i != min:
                nums[min] = nums[min] ^ nums[i]
                nums[i] = nums[min] ^ nums[i]
                nums[min] = nums[min] ^ nums[i]
        return nums

bs = SelectionSort()
nums = [1, 21, 52, 4, 26, 39]
print(bs.sort(nums))
