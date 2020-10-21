import pytest
import yaml
from decimal import *
from pytest_1.pythoncode.calculate import Calculator

#解析数据文件
def get_data():
    with open("./data/calc.yml",encoding='utf-8') as f:
        datas_yml = yaml.safe_load(f)
    add_date = datas_yml['add']['datas']
    add_ids = datas_yml['add']['ids']
    print(add_ids)
    print(add_date)
    return [add_date, add_ids]

#解析步骤文件
def get_step(filepath,a,b,expect):
    cal = Calculator()
    with open(filepath) as f:
        add_steps = yaml.safe_load(f)
    steps = add_steps["addstep"]
    for i in steps:
        if i =='add':
            assert expect == cal.add(a,b)
        if i =='add1':
            assert expect == cal.add1(a,b)


class TestCal:
    def setup(self):
        print("单个计算开始")
        self.cal = Calculator()

    def teardown(self):
        print("------> 单个计算结束")

    @pytest.mark.parametrize("a,b,expect",get_data()[0],ids=get_data()[1])
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
    #测试步骤驱动
    def test_step_add(self):
        get_step("./steps/step.yml",1,1,2)


