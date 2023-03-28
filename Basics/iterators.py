# words = [4, 3, 4, 5, 6]
#
# for a in words:
#     print(a)
#
# # in here words use iter function to iterate through elements
# print(dir(words))
#
# # we can have the iter object in seperately
# iter = iter(words)
# print(iter)
# print(next(iter))
#
# # iterate through reversed order
# riter = reversed(words)
# print(next(riter))


class RemoteControll:
    def __init__(self):
        self.channels = ["sirasa", "ITN", "AWS", "Net"]
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index == len(self.channels):
            raise stopIterating
        return  self.channels[self.index]

RC  = RemoteControll()
# this calls remote controller class __iter__ method
itr = iter(RC)
# this calls remote controller class __next__ method
print(next(RC))
print(next(RC))

# we can use also
print(next(itr))