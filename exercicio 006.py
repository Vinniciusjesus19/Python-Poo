import os
os.system('cls || clear') # Limpa o terminal.

class SaldoInsuficienteErro(Exception):
    def __init__(self, mensagem):
        self.mensagem = mensagem
        super().__init__(self.mensagem)

class ValorNegativoErro(Exception):
    pass

class Conta:
    def __init__(self, numero_conta: int, agencia: int) -> None:
        self.numero_conta = numero_conta
        self.agencia = agencia
        self._saldo = 0 #O underline em Python, serve para realizar um atributo protegido.

    @property
    def saldo(self):
        return self._saldo
    
    def sacar(self, valor):
        try:
            self.__verifica_sacar(valor)
        except ValorNegativoErro as error:
            return f'Eror {error}'
        
        self._saldo -= valor 
        return self._saldo

          
    def __verifica_sacar(self, valor):
        if valor > self.saldo:
         raise SaldoInsuficienteErro('Saldo insuficiente.')
    
    def depositar(self, valor):
        self._saldo += valor
        return self._saldo
    
    def __verificar_depositar(self, valor):
        if valor < 0: 
            raise ValorNegativoErro('Não pessível deposita valor menores que R$ 0,01')

class ContaCorrente(Conta):
    pass

class ContaPoupanca(Conta):
    pass

#Instanciar classes
conta_corrente = ContaCorrente(222, 333)
conta_corrente = ContaCorrente(444, 555)

print(conta_corrente.sacar(200))

print(conta_corrente._saldo)

print(conta_corrente.depositar(-200))

