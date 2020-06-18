import pytest
from pytest实战二 import calculator

@pytest.fixture(autouse=True)
def init_cal():
    '''
    :return:实例化Calculator
    '''
    print("\n开始计算")
    yield calculator.Calculator()
    print("\n计算结束")

