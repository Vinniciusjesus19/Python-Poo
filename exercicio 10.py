import pytest
from ...models.pessoa import Pessoa
from meu_projeto.models.endereco import Endereco
from meu_projeto.models.enums.sexo import Sexo
from meu_projeto.models.enums.unidade_federativa import UnidadeFederativa


# Modelo.
@pytest.fixture
def criar_pessoa():
    pessoa_1 = Pessoa("Marta", 22, Sexo.FEMININO,
        Endereco("Rua A.", 35, UnidadeFederativa.BAHIA))
    return pessoa_1

def test_pessoa_atributo_nome(criar_pessoa):
    assert criar_pessoa. nome == "Marta"

test_pessoa_atributo_nome

def test_pessoa_atributo_idade(criar_pessoa):
    assert criar_pessoa. idade == 22