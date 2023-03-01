import types


class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_lists = list_of_list
        self.current = 0
        self.current2 = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < len(self.list_of_lists):
            result = self.list_of_lists[self.current][self.current2]

            if self.current2 + 1 < len(self.list_of_lists[self.current]):
                self.current2 += 1
            else:
                self.current2 = 0
                self.current += 1
            return result
        else:
            raise StopIteration


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


def flat_generator(list_of_lists):
    cur = 0
    cur_1 = 0
    while cur < len(list_of_lists):
        result = list_of_lists[cur][cur_1]

        if cur_1 + 1 < len(list_of_lists[cur]):
            cur_1 += 1
        else:
            cur_1 = 0
            cur += 1
        yield result


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

    test_list = [[1,2,3], ['лист', 'вложен', 'в лист'], [True, False, None]]
    flatiterator = FlatIterator(test_list)
    print(list(flatiterator))
    print(list(flat_generator(test_list)))