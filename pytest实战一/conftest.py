import pytest
from pytest实战一 import calculator

@pytest.fixture(autouse=True)
def init_cal():
    '''
    实例化Calculator
    :return:
    '''
    return calculator.Calculator()
@pytest.fixture(autouse=True)
def setup():
    print("\n开始计算")

@pytest.fixture(autouse=True)
def teardown():
    print("计算结束")