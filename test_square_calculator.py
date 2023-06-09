from square_calculator import calculate_square

def test_calculate_square():
    assert calculate_square(2) == 4
    assert calculate_square(5) == 25
    assert calculate_square(0) == 0
