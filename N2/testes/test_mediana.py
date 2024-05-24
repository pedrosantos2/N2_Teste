from stat_funcs import StatsN2
import pytest


stat = StatsN2()

def test_mediana(numero_multimodal):
    res = stat.mediana(numero_multimodal)
    assert res == 6

@pytest.mark.parametrize("numero_multimodal,esperado", [([3,5,5,6], 5), ([5,12,5,12] ,8.5)])
def test_mediana(numero_multimodal,esperado):
    assert stat.mediana(numero_multimodal) == esperado

@pytest.mark.xfail
def test_mediaana(numero_multimodal):
    res = stat.mediana(numero_multimodal)
    assert res == 5