import pytest


# 如果有多个conftest文件，会自动调用最近的
@pytest.fixture(scope='session', params=['TOM',"jerry"])
def login(request):
    # 相当于setup
    print("登录操作")
    username = request.param
    # 相当于return
    yield "tom", "123456"
    # 相当于teardown
    print("退出操作")


@pytest.fixture()
def conn_db():
    print("连接数据库")

