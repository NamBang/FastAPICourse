"""Iterator
- Iterator is an object that ca be iterated using a loop. They give us one element at time. 
iterable: list, tuple, dictionary...
Iter is a object that alow we get each element.
Have two metho __iter__() and __next__() methods
- __iter__() return iterator object. It require setting for iterable and iterator to using for and in command
- __next__() return the next element. if it don't have any element, it raise the StopIteration exception.

iterator = iter(iterable)

=> iterator helps us reduce the using memory.
"""