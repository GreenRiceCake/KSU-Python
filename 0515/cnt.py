class Counter:
    def __init__(self, initValue=0):
        self.count = initValue
    def increment(self):
        self.count += 1
    def decrement(self):
        self.count -= 1
    def get_count(self):
        return self.count
    
a = Counter()
b = Counter()
c = Counter(100)
a1 = Counter()
a2 = Counter()
print(a.count)
a.increment()
print(a.count)
a.decrement()
print(a.count)