import pytest
from pytest实战一 import calculator

@pytest.fixture(autouse=True)
def init_cal():
    '''
    实例化Calculator
    :return:
    '''
    print("\n开始计算")
    yield calculator.Calculator()
    print("\n计算结束")