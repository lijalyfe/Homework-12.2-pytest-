from utils import arrs


def test_get():
    array = [1, 2, 'a', 'b']
    assert arrs.get(array, 0) == 1
    assert arrs.get(array, 2) == 'a'
    assert arrs.get(array, 4, default=0) == 0
    assert arrs.get(array, -1) is None
    assert arrs.get(array, -1, default='x') == 'x'


def test_my_slice():
    array = [1, 2, 'a', 'b', 3, 4]
    assert arrs.my_slice(array) == array
    assert arrs.my_slice(array, 2) == ['a', 'b', 3, 4]
    assert arrs.my_slice(array, -2) == [3, 4]
    assert arrs.my_slice(array, 0, 3) == [1, 2, 'a']
    assert arrs.my_slice(array, 2, -1) == ['a', 'b', 3]
    assert arrs.my_slice(array, end=4) == [1, 2, 'a', 'b']

