import pytest

@pytest.fixture(scope="session")
def s1():
    print('call s1')
    return 's1'

@pytest.fixture(scope="module", autouse=True)
def m1():
    print('call m1')
    return 'm1'

@pytest.fixture(scope="class")
def c1():
    print('call c1')
    return 'c1'

@pytest.fixture
def f1(f3):
    print('call f1')
    return 'f1' + f3

@pytest.fixture
def f3():
    print('call f3')
    return 'f3'

@pytest.fixture(autouse=True)
def a1():
    print('call a1')
    return 'a1'

@pytest.fixture
def f2():
    print('call f2')
    return 'f2'

def test_value(s1, f1, f2):
    print('Run test_value')
    print(f'{s1=} {m1=} {a1=} {f1=} {f2=}')
    res = m1()
    print('result of m1 = {res}')
    res = a1()
    print('result of a1 = {res}')
    assert False

@pytest.mark.usefixtures('c1')
class TestReturnValue:
    def test_method(self, f1):
        print(f'test_method: f1={f1}')
        print(f'test_method: m1={m1}')
        print(f'test_method: c1={c1}')
        assert False
    
