import pytest
x = 0

def test1():
    x = 1
    def test2():
        x = 3
        def test3():
            x = 3
            print(x)
        test3()
    test2()
test1()
