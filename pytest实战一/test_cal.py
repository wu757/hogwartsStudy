import yaml


class TestCal():
    # @pytest.mark.parametrize("a,b,c",[(3,4,7),(3,5,8)])
    def test_add(self,a,b,expect,init_cal):
        assert init_cal.add(a,b)==expect

    def test_sub(self,a,b,expect,init_cal):
        assert init_cal.sub(a,b)==expect

    def test_mul(self,a,b,expect,init_cal):
        assert init_cal.mul(a,b)==expect

    def test_div(self, a, b, expect, init_cal):
        assert init_cal.div(a, b) == expect