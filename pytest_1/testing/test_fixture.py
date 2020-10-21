import pytest


# 直接把装饰器函数传入参数可实现调用，可以调用返回的参数
# 可以使用多个fixture
# 多个fixture当是autouse=true的时候，执行顺序是根据方法的名字
def test_case1(login,conn_db):
	# 直接打印函数名字，即可获取返回值
	print(login)
	print("测试用例1")


# 使用装饰器进行fixture调用，缺点是不能使用返回的参数
@pytest.mark.usefixtures('login')
def test_case2():
	print("测试用例2")


def test_case3():
	print("测试用例3")