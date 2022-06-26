Generator is functional that return the iterator and it can loop.
yeild stop functional and all local variables and state will remain for next yeild.
when functional end , StopIteration will happen when we try to call function.

***************************Generator function*************************************
- Have the yield keyword in the function

def generator_func(n=0):
    yield n
    n += 1

*************************** Generator Expression********************************
- The same the comprehension expression but Generator Expression use the () instead of [].
expample:
generator_ojb = (x**2 for x in Myarray)
comprehension_list = [x**2 for x in Myarray]