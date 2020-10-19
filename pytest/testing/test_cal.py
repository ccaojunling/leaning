import pytest

from leaning.pytest.pythoncode import Calculator


class TestCal:
    def setup(self):
        print("单个计算开始")
        self.cal = Calculator()

    def teardown(self):
        print("------> 单个计算结束")

    @pytest.mark.parametrize("a,b,expect",[[1,1,2],[100,100,200],[0.1,0.1,0.2]],ids=["整数","大数","小数"])
    def test_add(self,a,b,expect):
        result = self.cal.add(a,b)
        assert result == expect
