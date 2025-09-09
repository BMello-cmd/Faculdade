from pessoa import Pessoa 

class Conta:
    def __init__(self, agencia, tipo_conta, numconta, saldo, pessoa):
        self.agencia = agencia
        self.tipo_conta = tipo_conta
        self.numconta = numconta
        self.saldo = saldo
        self.pessoa = pessoa
        
    def exibir_dados_conta(self):
        print(f'Dados da conta: Agencia: {self.agencia}, Tipo de conta: {self.tipo_conta}, Saldo disponivel: {self.saldo}, numero da conta: {self.numconta}.')
        
    def exibir_saldo(self):
        print(f'{self.saldo}')    
    
    def exibir_dados_pessoais(self):
        print(f'{self.pessoa.nome}, {self.pessoa.sobrenome}')
        
