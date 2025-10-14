print("Hello World")

#Questâo 2
numero = int(input('digite um numero: '))
print('o numero é:', numero)

#questao 3
valor1 = int(input('digite o valor 1: '))
valor2 = int(input('digite o valor 2: '))

soma= valor1 + valor2

print('o resultado é', soma)

#questao 4
nota1 = int(input('digite o valor 1: '))
nota2 = int(input('digite o valor 2: '))
nota3 = int(input('digite o valor 3: '))
nota4 = int(input('digite o valor 4: '))

media = (nota1 + nota2 + nota3 + nota4)/4
print('a media é', media)

#questao 5
nome = input(f"digite seu nome: ")
senha = input(f"digite sua senha: ")

while senha == nome:
    print('Erro! nome não pode ser igual a senha.')
    senha = input(f"digite sua senha: ")
print('conta criada com sucesso!')