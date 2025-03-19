from src import testing_operation
import pytest

def test_add():
    assert testing_operation.add(1,2) == 3
    assert testing_operation.add(3,4) == 7

def test_sub():
    assert testing_operation.sub(1,2) == -1
    assert testing_operation.sub(3,4) == -1