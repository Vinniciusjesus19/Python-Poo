import pytest
from projeto.models.pessoa import pessoa

@pytest
def pessoa_valida():
    pessoa = pessoa("Marta" , 21)
    return pessoa

def test_pessoa_alterar_nome_valido(pessoa_valida):
    assert pessoa_valida.nome == "Marta"

def test_pessoa_idade_negativa_retorna_mensagem_excecao(pessoa_valida):
    with pytest.raises(ValueError, match= "Idade não pode ser negativa. "):
        pessoa("Marta" , -1)
