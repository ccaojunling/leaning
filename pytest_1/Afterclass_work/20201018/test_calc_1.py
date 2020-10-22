import pytest
from pytest_1.pythoncode.calculate import Calculator
import yaml


def get_data():
	with open("test_1.yml",encoding='utf-8') as f:
		all_datas = yaml.safe_load(f)
	full_datas= all_datas["datas"]
	return full_datas


class TestCa():
	@pytest.mark.run(order=0)
	@pytest.mark.parametrize("a,b,expect",get_data()["add_int"],ids=get_data()["add_int_ids"])
	def test_add(self,fixture_cacl,a,b,expect):
		result = fixture_cacl.add(a,b)
		assert expect == result

	@pytest.mark.parametrize("a,b,expect", get_data()["add_float"], ids=get_data()["add_float_ids"])
	@pytest.mark.run(order=1)
	def test_add_float(self, fixture_cacl, a, b, expect):
		result = fixture_cacl.add(a, b)
		assert round(result,2) == expect

	@pytest.mark.parametrize("a,b,expect", get_data()["sub"], ids=get_data()["sub_ids"])
	@pytest.mark.run(order=3)
	def test_sub(self, fixture_cacl, a, b, expect):
		result = fixture_cacl.sub(a, b)
		assert round(result,5) == expect

	@pytest.mark.parametrize("a,b,expect", get_data()["mul"], ids=get_data()["mul_ids"])
	@pytest.mark.run(order=4)
	def test_mul(self, fixture_cacl, a, b, expect):
		result = fixture_cacl.mul(a, b)
		assert round(result, 5) == expect

	@pytest.mark.parametrize("a,b,expect", get_data()["div"], ids=get_data()["div_ids"])
	@pytest.mark.run(order=2)
	def test_div(self, fixture_cacl, a, b, expect):
		try:
			result = fixture_cacl.div(a, b)
		except ZeroDivisionError:
			print("除数不能为0")
		else:
			assert result == expect


