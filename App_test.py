# test_app.py
import pytest
from App import add, subtract, multiply

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(10, 20) == -10
    assert subtract(7, 7) == 0

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 5) == -5
    assert multiply(0, 100) == 0
    assert multiply(7, 0) == 0

# Ví dụ về một test case cố ý bị lỗi để bạn thấy CI/CD sẽ thất bại
# def test_add_fail_example():
#     assert add(1, 1) == 3 # Lỗi này sẽ khiến test thất bại