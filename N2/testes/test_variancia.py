from stat_funcs import StatsN2
import pytest


stat = StatsN2()

def test_variancia(numero_multimodal):
    res = stat.variancia(numero_multimodal)
    assert res == 1.2380952380952381

@pytest.mark.parametrize("numero_multimodal,esperado", [([3,5,5,6], 4.75), ([5,12,5,12], 8.5)])
def test_variancia(numero_multimodal,esperado):
    assert stat.variancia(numeros_amodal) == esperado

@pytest.mark.xfail
def test_variancia(numero_multimodal):
    res = stat.variancia(numero_multimodal)
    assert res == 4