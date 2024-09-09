import os
from enum import Enum

class Sexo(Enum):
    """Definindo valores do Enum. """
    MASCULINO = "Masculino"
    FEMININO = "Feminino"

class Pessoa:
    def __init__(self, nome: str idade: int, sexo: Sexo) -> None:
    """Construtor. ""
        self.nome = nome
        self.idade = idade
        self.sexo = sexo

    def __str__(self) -> str:
    """Equivalente ao tostring() do Java."""
            return (f"\nNome: {self.nome}"
            f"\nIdade: {self.idade}"
            f"\nSexo: {self.sexo.value}"
                    )

# Instanciando classe Pessoa.
os.system("cls | | clear")