from stat_funcs import StatsN2
import pytest


stat = StatsN2()

def test_skew(numero_multimodal):
    res = stat.skew(numero_multimodal)
    assert res == "Distribuição negativa"


@pytest.mark.parametrize("numero_multimodal,esperado", [([3,5,5,6], "Distribuição Positiva"), ([5,12,5,12] , "Distribuição Positiva")])
def test_skew(numero_multimodal,esperado):
    assert stat.skew(numero_multimodal) == esperado

@pytest.mark.xfail
def test_skew(numero_multimodal):
    res = stat.skew(numero_multimodal)
    assert res == "Distribuição Positiva"