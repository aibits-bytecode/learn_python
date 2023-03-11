class Cal:
    def average(self, *m):
        average = 0
        for i in m:
            average = average + i
        return average/ len(m)
cal = Cal()
print(cal.average(2,3))
