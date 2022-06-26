def infinite_naturals():
    start = 1
    
    while start < 10:
        yield start
        start += 1

numbers = list(infinite_naturals())
print(numbers)

for item in numbers:
    print(item)