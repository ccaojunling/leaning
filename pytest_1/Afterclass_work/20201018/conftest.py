import pytest
from pytest_1.pythoncode.calculate import Calculator


@pytest.fixture(scope='module')
def fixture_cacl():
	cal = Calculator()
	print("计算开始")
	yield cal
	print("计算结束")


def pytest_collection_modifyitems(session,config,items):
	for item in items:
		item.name = item.name.encode("utf-8").decode('unicode-escape')
		item._nodeid = item.nodeid.encode("utf-8").decode('unicode-escape')