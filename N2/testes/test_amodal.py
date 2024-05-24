from stat_funcs import StatsN2
import pytest


stat = StatsN2()



def test_amodal(numeros_amodal):
    res = stat.amodal(numeros_amodal)
    assert res == "Existe moda"

@pytest.mark.parametrize("numeros_amodal,esperado", [([3,5,5,6], "Existe moda"), ([5,12,5,6], "Existe moda")])
def test_amodal(numeros_amodal,esperado):
    assert stat.amodal(numeros_amodal) == esperado

@pytest.mark.xfail
def test_amodal(numeros_amodal):
    res = stat.amodal(numeros_amodal)
    assert res == "Não existe moda"