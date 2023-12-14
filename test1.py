import pytest

def add(a,b):
    return(a+b)

def test_m1():
    assert add(1,2) == 3
