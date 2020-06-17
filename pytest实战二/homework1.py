import pytest
import yaml

with open("./data_cal.yaml",'rb') as f:
    test_data=yaml.safe_load(f)

class TestCal():
    @pytest.mark.parametrize("a,b,expect",test_data["add"])
    def test_add(self,a,b,expect,init_cal):
        assert init_cal.add(a,b)==expect

    @pytest.mark.parametrize("a,b,expect", test_data["sub"])
    def test_sub(self,a,b,expect,init_cal):
        assert init_cal.sub(a,b)==expect

    @pytest.mark.parametrize("a,b,expect", test_data["mul"])
    def test_mul(self,a,b,expect,init_cal):
        assert init_cal.mul(a,b)==expect

    @pytest.mark.parametrize("a,b,expect", test_data["div"])
    def test_div(self, a, b, expect, init_cal):
        assert init_cal.div(a, b) == expect

    @pytest.mark.parametrize("a,b,expect", test_data["add"])
    def check_add(self, a, b, expect, init_cal):
        assert init_cal.add(a, b) == expect

    @pytest.mark.parametrize("a,b,expect", test_data["sub"])
    def check_sub(self,a,b,expect,init_cal):
        assert init_cal.sub(a,b)==expect

    @pytest.mark.parametrize("a,b,expect", test_data["mul"])
    def check_mul(self,a,b,expect,init_cal):
        assert init_cal.mul(a,b)==expect

    @pytest.mark.parametrize("a,b,expect", test_data["div"])
    def check_div(self, a, b, expect, init_cal):
        assert init_cal.div(a, b) == expect