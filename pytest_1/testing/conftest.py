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


# 设置编码，
def pytest_collection_modifyitems(session,config,items):
    for item in items:
        item.name = item.name.encode("utf-8").decode('unicode-escape')
        item._nodeid = item.nodeid.encode("utf-8").decode('unicode-escape')

