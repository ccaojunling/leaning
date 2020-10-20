import pytest
from decimal import *
from leaning.pytest.pythoncode.calculate import Calculator

class TestCal:
    def setup(self):
        print("单个计算开始")
        self.cal = Calculator()

    def teardown(self):
        print("------> 单个计算结束")

    @pytest.mark.parametrize("a,b,expect",[[1,1,2],[100000000000000000,100000000000000000,200000000000000000],[0.0000000000000000001,0.0000000000000000002,0.0000000000000000003]],ids=["intnum","bignum","too_smallnum"])
    def test_add(self,a,b,expect):
        result = self.cal.add(a,b)
        assert result == expect

    @pytest.mark.parametrize("a,b,expect",[[0.1,0.2,0.3]],ids=["floatnum"])
    def test_float_add(self,a,b,expect):
        result = self.cal.add(a,b)
        assert round(result,2) == expect

    @pytest.mark.parametrize("a,b,expect",[[0.1,2,0.05],[1,1,1],[2,3,0.667],[1000000000000000000000,3,333333333333333333333.333],[1,0,0]],ids=["floatnum","intnum","div***","bignum","zero"])
    def test_div(self,a,b,expect):
        # with pytest.raises(ZeroDivisionError):
        #     result = self.cal.div(a,b)
        try:
            result = self.cal.div(a,b)
        except ZeroDivisionError:
            print("除数不能为0")
        else:
            result = self.cal.div(a, b)
            assert round(result, 3) == expect

