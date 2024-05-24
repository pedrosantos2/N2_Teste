from stat_funcs import StatsN2
import pytest


stat = StatsN2()

def test_media_ponderada(numeros_amodal, pesos):
    res = stat.media_ponderada(numeros_amodal,pesos)
    assert res == 2.784591417646226

@pytest.mark.parametrize("numeros_amodal, pesos,esperado", [([3,5,5,6],[2,3,4,5],4.75), ([5,12,5,12],[4,5,6,7] ,8.5)])
def test_media_ponderada(numeros_amodal,pesos,esperado):
    assert stat.media_ponderada(numeros_amodal,pesos) == esperado

@pytest.mark.xfail
def test_media_ponderada(numeros_amodal,pesos):
    res = stat.media_ponderada(numeros_amodal,pesos)
    assert res == 5