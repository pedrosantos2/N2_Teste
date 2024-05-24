
import pytest

@pytest.mark.rodarEmGrupo


@pytest.fixture
def numeros_amodal():
    return [2,4,4,2]

@pytest.fixture
def pesos():
    return [10.5,7,20.7,32.41]

@pytest.fixture
def numero_unimodal():
    return [2,4,4,5,6,7,8,9]

@pytest.fixture
def numero_multimodal():
    return [4,5,5,6,6,7,7]

@pytest.fixture
def varianca():
    return 1.2380952380952381