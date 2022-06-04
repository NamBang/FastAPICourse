from typing import Union, Callable

count = 5
print(type(count))

def total_price(price_1: int, price_2: int):
    return f"Your total bill is USB {price_1 + price_2}"

price = total_price(30, 40)

x: list[Union[int, float]] = [2, 3, 4.1, 5, 6]

print(x)

def inr_to_usb(value:float) -> Union[int, None]:
    try:
        conversion_factor = 75
        value = value / conversion_factor
        return value
    except TypeError:
        return None

print(inr_to_usb('23'))

def smart_divide(func: Callable[[int, int], float]):
    def inner(a,b):
        if b == 0:
            print("Whoops! Division by 0")
            return None
        return func(a,b)
    return inner

@smart_divide
def dive(a, b):
    print(a/b)

dive(10,3)
dive(10,0)

