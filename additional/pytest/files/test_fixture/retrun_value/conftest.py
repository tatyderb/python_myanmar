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
    
@pytest.fixture(scope='module')
def module_variable(request):
    current_host = getattr(request.module, "host", "gmail.com")
    # тут мы можем установить соединение current_host
    print(f'connect to {current_host=}')
