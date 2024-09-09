import os
os.system('cls || clear')

from enum import Enum

class Sexo(enumerate):
    MASCULINO = "Masculino"
    FEMININO = "Feminino"

class Pessoa:
    def __init__ (self, nome: str, idade: int, sexo: Sexo) -> None:
        self.nome = nome
        self.idade = idade
        self.sexo = sexo

    def __str__ (self) -> str:
        return (f"\nNome: {self.nome}"
                f"\nIdade: {self.idade}"
                f"\nSexo: {self.sexo}"
            )

# Instanciando classe Pessoa.
pessoa_1 = Pessoa("Marta", 22, Sexo.FEMININO)

print(pessoa_1)



