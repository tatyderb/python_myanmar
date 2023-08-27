import pytest

def test_value_implict(s1, f1, f2):
    print('Run test_value_implict')
    print(f'{s1=} {a1=} {f1=} {f2=}')
    assert False

def test_value_explict(s1, f1, f2, m1, a1, c1):
    print('Run test_value_explict')
    print(f'{s1=} {m1=} {c1=} {a1=} {f1=} {f2=}')
    assert False
    
@pytest.mark.usefixtures('c1')
class TestReturnValue:
    def test_method(self, f1):
        print(f'test_method: f1={f1}')
        assert False
        
def test_default_value(module_variable):
    assert False
 
