from src import math_operation

def test_add():
    assert math_operation.add(1,2) == 3
    assert math_operation.add(3,4) == 7

def test_sub():
    assert math_operation.sub(1,2) == -1
    assert math_operation.sub(3,4) == -1