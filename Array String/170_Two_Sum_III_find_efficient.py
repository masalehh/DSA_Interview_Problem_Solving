class TwoSumIII:
    def __init__(self):
        self.nums = []
        self.possible_sums = set()

    def add(self, value):
        for num in self.nums:
            self.possible_sums.add(num + value)

        self.nums.append(value)

    def find(self, target):
        return target in self.possible_sums


ts = TwoSumIII()
ts.add(10)
ts.add(7)
ts.add(3)
print(ts.find(10))
print(ts.find(11))


# Time Complexity
#
# Worst Case: O(n)
#
# Space Complexity
#
# Auxiliary Space per add(): O(1)
#
# Total Space: O(n²)
#
# find(target)
# Time Complexity
# Average Case: O(1)
