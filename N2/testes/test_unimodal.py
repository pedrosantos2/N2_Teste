from stat_funcs import StatsN2
import pytest


stat = StatsN2()

def test_unimodal(numero_unimodal):
    res = stat.unimodal(numero_unimodal)
    assert res == 4

@pytest.mark.parametrize("numero_unimodal,esperado", [([3,5,5,6], 5), ([5,5,5,12], 5)])
def test_unimodal(numero_unimodal,esperado):
    assert stat.unimodal(numeros_amodal) == esperado

@pytest.mark.xfail
def test_unimodal(numero_unimodal):
    res = stat.unimodal(numero_unimodal)
    assert res == 3