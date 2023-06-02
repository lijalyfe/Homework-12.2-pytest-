from utils import arrs


def test_get():
    array = [1, 2, 'a', 'b']
    assert arrs.get(array, 0) == 1
    assert arrs.get(array, 2) == 'a'
    assert arrs.get(array, 4, default=0) == 0
    assert arrs.get(array, -1) is None
    assert arrs.get(array, -1, default='x') == 'x'


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
