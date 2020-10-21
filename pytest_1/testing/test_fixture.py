import pytest


@pytest.fixture
def login():
	# 相当于setup
	print("登录操作")
	# 相当于return
	yield "tom", "123456"
	# 相当于teardown
	print("退出操作")


@pytest.fixture()
def conn_db():
	print("连接数据库")


# 直接把装饰器函数传入参数可实现调用，可以调用返回的参数
# 可以使用多个fixture
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