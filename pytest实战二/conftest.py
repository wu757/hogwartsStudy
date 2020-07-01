import pytest
import yaml

from pytest实战二 import calculator


@pytest.fixture(autouse=True)
def init_cal():
    '''
    :return:实例化Calculator
    '''
    print("\n开始计算")
    yield calculator.Calculator()
    print("\n计算结束")


def pytest_addoption(parser):
    parser.addoption(
        "--env", action="store", default="test", help="choose your environment: dev or test or st"
    )


@pytest.fixture
def cmdopt(request):
    data_path = "datas.yaml"
    myenv = request.config.getoption("--env", default="test")
    if myenv == "test":
        print("测试环境")
    elif myenv == "dev":
        print("开发环境")
    elif myenv == "st":
        print("集成环境")

    with open(data_path, "rb") as f:
        datas = yaml.safe_load(f)
    data = datas[myenv]
    return data
