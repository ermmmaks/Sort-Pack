from sort_pack.pyramid_sort_alg import build_pyramid

# обычные unit-тесты

test_array = [0, 9, 3, 5]


def test_first():
    assert build_pyramid(test_array) == [0, 3, 5, 9]


second_array = [766, 1, 9023, 63, 4248]


def test_second():
    assert build_pyramid(second_array) != [9023, 1, 766, 4248, 63]
