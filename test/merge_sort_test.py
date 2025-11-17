from sort_pack.merge_sort import merge_sort
from conftest import random  # noqa F401
import pytest


# обычные unit-тесты

test_array = [0, 9, 3, 5]


def test_first():
    assert merge_sort(test_array) == [0, 3, 5, 9]


second_array = [766, 1, 9023, 63, 4248]


def test_second():
    assert merge_sort(second_array) != [9023, 1, 766, 4248, 63]


# крайние случаи


@pytest.mark.parametrize(
    ["array", "expected"],
    [([], []), ([0], [0]), ([-1, 2, -3], [-3, -1, 2]), ([1, 2, 1], [1, 1, 2])],
)
def test_with_expected(array, expected):
    assert merge_sort(array) == expected


# property-based


def test_random_array(rndm):  # noqa F811
    assert merge_sort(rndm) == sorted(rndm)
