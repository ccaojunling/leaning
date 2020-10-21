import pytest


@pytest.mark.login
def login1():
    print("登录用例1")


@pytest.mark.login
def login2():
    print("登录用例2")


@pytest.mark.search
def search1():
    print("搜索用例2")


@pytest.mark.search
def search2():
    print("搜索用例2")

# pytest -m login
