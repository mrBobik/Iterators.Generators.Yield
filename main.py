import types


# TODO Task 1:
class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.counter = -1
        self.counter_in = 0

    def __iter__(self):
        self.counter += 1
        self.counter_in = 0
        return self

    def __next__(self):
        while self.counter - len(self.list_of_list) and self.counter_in == len(self.list_of_list[self.counter]):
            iter(self)
        if self.counter == len(self.list_of_list):
            raise StopIteration
        self.counter_in += 1
        return self.list_of_list[self.counter][self.counter_in - 1]


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


# TODO Task 2:
def flat_generator(list_of_list, tree_types=(list, tuple)):
    if isinstance(list_of_list, tree_types):
        for i in list_of_list:
            for j in flat_generator(i, tree_types):
                yield j
    else:
        yield list_of_list


def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_1()
    test_2()
