import pytest

@pytest.mark.skip
@pytest.mark.smoke
def test_firstProgram():
    msg="Hello"
    assert msg=="hi","test failed as not matched"

def test_secondProgram():
    a=6
    b=4
    assert b+2==6,"addition do not match"

@pytest.fixture()
def setup():
    print("i will be executing first")
    yield
    print("i wiil be executing on last")

def test_fixtureDemo(setup):
    print("i will executre in fixture demo")



