from stat_funcs import StatsN2
import pytest


stat = StatsN2()

def test_dpadrao(varianca):
    res = stat.dpadrao(varianca)
    assert res == 1.1126972805283737

@pytest.mark.parametrize("variancia,esperado", [(1.2380952380952381, 2.56), (5.254, 2,292160552840922)])
def test_dpadrao(variancia,esperado):
    assert stat.dpadrao(variancia) == esperado

@pytest.mark.xfail
def test_dpadrao(varianca):
    res = stat.dpadrao(varianca)
    assert res == 2