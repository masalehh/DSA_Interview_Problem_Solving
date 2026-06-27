from collections import defaultdict


class TwoSumIII:
    def __init__(self):
        self.freq_counts = defaultdict(int)

    def add(self, number: int) -> None:
        self.freq_counts[number] += 1

    def find(self, value: int) -> bool:
        for num, frequency in self.freq_counts.items():
            complement = value - num
            if complement in self.freq_counts:
                if num != complement or frequency > 1:
                    return True

        return False


ts = TwoSumIII()

ts.add(1)
ts.add(3)
ts.add(5)

print(ts.find(4))

print(ts.find(9))


ts.add(1)
ts.add(3)
ts.add(5)
ts.add(7)

print(ts.find(4))    # 1 + 3
print(ts.find(8))    # 1 + 7 or 3 + 5
print(ts.find(10))   # 3 + 7
print(ts.find(100))  # No pair