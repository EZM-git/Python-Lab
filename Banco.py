class Conta:
    def __init__(self, num_conta, nome):
        self._num_conta =  num_conta
        self.nome = nome
        self.__saldo = 0
    
    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, valor):
        self.__saldo = valor

    def depositar_valores(self, valor):
        self.__saldo += valor

    def sacar_valores(self, valor):
        if self.__saldo > 0:
            self.__saldo -= valor
        else:
            print("Saldo Insuficiente!")

    def __str__(self):
        return f"A conta número: {self._num_conta} possui o saldo atual no valor de: R${self.__saldo}"



class ContaCorrente(Conta):
    def __init__(self, limite, num_conta, nome):
        super().__init__(num_conta, nome)
        self.__limite = limite

    def sacar_valores_especial(self, valor):
        if -1*self.__limite >= self._Conta__saldo - valor:
            self._Conta__saldo -= valor

class Poupanca(Conta):
    def __init__(self, num_conta, nome):
        super().__init__(num_conta, nome)
        self._rend_mensal = 6

    @property
    def rend_mensal(self):
        return self._rend_mensal
    
    @rend_mensal.setter
    def rend_mensal(self, valor):
        self._rend_mensal = valor

    def rendimento(self):
        self._Conta__saldo += (self._Conta__saldo * self._rend_mensal)/100
        print(f"Saldo Atualzado: R${self._Conta__saldo}")


class Poupex(Poupanca):
    def __init__(self, num_conta, nome):
        super().__init__(num_conta, nome)


    def rendimento_extra(self):
        self._Conta__saldo += self._Conta__saldo/100

    
conta_normal = Conta("1234-56", "Matheus")
conta_normal.depositar_valores(213)
conta_normal.sacar_valores(111)
print(conta_normal)
conta_corrente = ContaCorrente(2000, "4321-65", "Yuri")
conta_corrente.depositar_valores(123)
conta_corrente.sacar_valores(123)
conta_corrente.sacar_valores_especial(123)
print(conta_corrente)
conta_poupanca = Poupanca("2134-21", "Otávio")
conta_poupanca.depositar_valores(3211)
conta_poupanca.rendimento
print(conta_poupanca)
conta_poupex = Poupex("3123-12", "Nathan")
conta_poupex.depositar_valores(1234)
conta_poupex.rendimento()
conta_poupex.rendimento_extra()
print(conta_poupex)
