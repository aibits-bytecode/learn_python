class LinearSearch:

    def search(self, nums, finder):
        i = 0
        while i < len(nums):
            if nums[i] == finder:
                return i
            i += 1
        return -1

nums = [1, 2, 5, 4, 6, 9]

ls = LinearSearch()
print(ls.search(nums, 9))
