import pytest


# 失败重跑 pytest-rerunfailures
# pytest **.py --reruns 5
# pytest --reruns 5 --reruns-delay 1
# pytest --reruns 5 --only-rerun AssertionError

# 也可以用装饰器
@pytest.mark.flaky(reruns=5)
def test_example():
    import random
    assert random.choice([True, False])

# 统计assert异常,pytest-assume,多重校验
@pytest.mark.parametrize(('x', 'y'), [(1, 1), (1, 0), (0, 1)])
def test_simple_assume(x, y):
    pytest.assume(x == y)
    pytest.assume(True)
    pytest.assume(False)

# 电脑分布式并发执行，pytest-xdist，不要让测试用例有顺序或者有依赖，要不并发执行会出错
# pytest **.py -n  3

# 控制用例执行用例
# @pytest.mark.run(order=1)

