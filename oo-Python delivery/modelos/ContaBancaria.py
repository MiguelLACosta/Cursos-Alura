class ContaBancaria:
    def __init__(self,titular,saldo):
        self._titular = titular.title()
        self._saldo = float(saldo)
        self._ativo = False
    
    def __str__(self):
        return f'Bem vindo {self._titular}! Seu saldo é de R${self._saldo}'
    
    @classmethod
    def ativar_conta(cls, conta):
        conta._ativo = True

conta1 = ContaBancaria('Miguel',1000)
conta2 = ContaBancaria('maria',2000)
conta3 = ContaBancaria('joao',5000)

print(conta1)
print(conta2)
print(f'Antes de ativar: conta ativa? {conta3._ativo}')
ContaBancaria.ativar_conta(conta3)
print(f'Depois de ativar: conta ativa? {conta3._ativo}')