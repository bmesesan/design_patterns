from abc import ABC
from collections.abc import Iterable


class SumObject(Iterable, ABC):
    @property
    def sum(self):
        my_sum = 0
        for elem in self:
            if issubclass(type(elem), SumObject):
                my_sum += elem.sum
            else:
                my_sum += elem
        return my_sum


class SingleValue(SumObject):
    def __init__(self, value):
        self.value = value
    
    def __iter__(self):
        yield self.value


class ManyValues(list, SumObject):
    def __init__(self, value=None):
        super().__init__()
        if value:
            self.append(value)


def main():
    single_value = SingleValue(11)
    other_values = ManyValues()
    other_values.append(22)
    other_values.append(33)
    # make a list of all values
    all_values = ManyValues()
    all_values.append(single_value)
    all_values.append(other_values)
    assert all_values.sum == 66


if __name__ == "__main__":
    main()