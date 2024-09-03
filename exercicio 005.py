import os
os.system('cls || clear')

from abc import ABC, abstractmethod
import os
os.system('cls || clear')

class Funcionario(ABC):
    def __init__(self, nome: str, idade: int, salario: float, email: str, endereco: str) -> None:
        self.nome = nome
        self.idade = idade
        self.salario = salario
        self.email = email
        self.endereco = endereco

    @abstractmethod
    def calcular_salario(self) -> float:
        pass


class Endereco(Funcionario):
    def calcular_salario(self) -> float:
        logradouro: str
        numero: str
        complemento: str
        cep: str
        cidade: str

class Engenheiro(Funcionario):
    def calcular_salario(self) -> float:
         BONIFICACAO = 1.2 #Equivalente a 20% de alguma coisa. 
         salario_final = self.salario * BONIFICACAO
         return salario_final

class Medico(Funcionario):
    def calcular_salario(self) -> float:
        DESCONTO = 0.2
        salario_final = self.salario * DESCONTO
        return salario_final


engenheiro1 = Engenheiro('Miguel', 25, 3000.0, 'miguel@123', 'Rua 35 n° 10')
print(f'Nome: {engenheiro1.nome}')
print(f'Idade: {engenheiro1.idade}')
print(f'Salário com bonificação: {engenheiro1.calcular_salario()}')
print(f'Email: {engenheiro1.email}')
print(f'Endereço: {engenheiro1.endereco}')

print('\n')

medico1 = Medico('Ana', 25, 3500.0, 'ana@1000', 'rua 35 nº 11')
print(f'Nome: {medico1.nome}')
print(f'Idade: {medico1.idade}')
print(f'Salário com desconto: {medico1.calcular_salario()}')
print(f'Email: {medico1.email}')
print(f'Endereço: {medico1.endereco}')