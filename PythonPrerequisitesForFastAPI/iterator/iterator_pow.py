class PowNumber():
    def __init__(self, base_number):
        """_summary_
        int() return 0
        Args:
            base_number (_type_): _description_
        """
        self.n = int()
        self.base_number = base_number
    
    def __iter__(self):
        """_summary_

        Returns:
            _type_: return iterator object
        """
        return self

    def __next__(self):
        n = self.n
        self.n += 1
        return self.base_number**n

pow_number = iter(PowNumber(2))

print(type(pow_number))

print(next(pow_number))
print(next(pow_number))
print(next(pow_number))
print(next(pow_number))
    