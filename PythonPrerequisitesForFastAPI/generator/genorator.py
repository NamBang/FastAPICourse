def generator_func(n=0):
    while n < 10:
        yield n
        n += 1

generator_obj = generator_func(1)

print(type(generator_obj))