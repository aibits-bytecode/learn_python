class BinarySearch:

    def search(self, nums, finder):
        l = 0
        u = len(nums)-1

        while l<=u:
            if nums[(l+u)//2] == finder:
                return (l+u)//2
            else:
                if nums[(l+u)//2] < finder:
                    l = ((l+u)//2)+1
                else:
                    u = ((l+u)//2)-1
        return -1


nums = [1, 2, 5, 14, 26, 39]

ls = BinarySearch()
print(ls.search(nums, 1))