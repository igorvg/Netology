class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.list_finish = list()
        self.counter_exit = 0
        self.main_counter = 0
        self.second_counter = 0
        return self

    def __next__(self):
        if self.main_counter == len(self.list_of_list) - 1 and \
                self.second_counter == len(self.list_of_list[self.main_counter]):
            raise StopIteration
        if self.second_counter >= len(self.list_of_list[self.main_counter]):
            self.main_counter += 1
            self.second_counter = 0

        item = self.list_of_list[self.main_counter][self.second_counter]
        self.second_counter += 1
        return item


def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None],
        [1]
    ]

    for flat_iterator_item, check_item in zip(FlatIterator(list_of_lists_1),
                                              ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, 1]):
        assert flat_iterator_item == check_item




def test_2():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!'], \
        'Error test3'



