class NaturalNumbers:
    def __init__(self):
        self.n = 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        num = self.n
        self.n += 1
        return num

num = iter(NaturalNumbers())
print(type(num))
print(next(num))
print(next(num))