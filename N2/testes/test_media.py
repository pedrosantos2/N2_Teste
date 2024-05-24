from stat_funcs import StatsN2
import pytest


stat = StatsN2()


def test_media(numeros_amodal):
    res = stat.media(numeros_amodal)
    assert res == 3

@pytest.mark.parametrize("numeros_amodal,esperado", [([3,5,5,6], 4.75), ([5,12,5,12], 8.5)])
def test_media(numeros_amodal,esperado):
    assert stat.media(numeros_amodal) == esperado

@pytest.mark.xfail
def test_media(numeros_amodal):
    res = stat.media(numeros_amodal)
    assert res == 4