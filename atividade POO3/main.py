from pessoa import Pessoa
from conta import Conta

cliente = Pessoa('Bruno', 'Henrique', '000.000.000-00', 'algum@gmail.com', '888888888')


conta = Conta('Mastercard', 'Débito','830', 3000, cliente)
conta.exibir_dados_conta()
conta.exibir_dados_pessoais()
conta.exibir_saldo()


