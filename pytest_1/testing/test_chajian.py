import pytest


# 失败重跑 pytest-rerunfailures
# pytest **.py --reruns 5
# pytest --reruns 5 --reruns-delay 1
# pytest --reruns 5 --only-rerun AssertionError
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

# 电脑分布式并发执行，pytest-xdist
# pytest **.py -n  3


