# Since implementing a singleton is easy,
# you have a different challenge: write a function called is_singleton() .
# This method takes a factory method that returns an object and it's up to you
# to determine whether or not that object is a singleton instance.

def is_singleton(factory):
    # todo: call factory() and return true or false
    # depending on whether the factory makes a
    # singleton or not
    test_1 = factory()
    test_2 = factory()
    return test_1 is test_2