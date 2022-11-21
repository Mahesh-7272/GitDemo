#any pytest file should start with test
#any function start with test
import pytest


@pytest.mark.smoke
def test_firstProgram():
    print("hello")

def test_SecondgreetCreditcard():
    print("Good morning")