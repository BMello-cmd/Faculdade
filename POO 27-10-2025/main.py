print("Digite as notas (digite -1 para parar):")

notas = []


while True:
    nota = int(input("Digite um numero: "))
    
    if nota == -1:
        break
    
    notas.append(nota)


quantidade = len(notas)
print(f"a) Quantidade de notas lidas: {quantidade}")

print(f"b) notas na forma original: ", end="")
for nota in notas:
    print(f"{nota:.1f} ", end="")
print()

print("c) notas na forma inversa:")
for i in range(len(notas)-1, -1, -1):
    print(f"   {notas[i]}")

soma = sum(notas)
print(f"d) Soma: {soma}")

if quantidade > 0:
    media = soma / quantidade
    print(f"e) Média: {media:.2f}")
else:
    media = 0
    print("ERRO!")

acima_media = 0
for nota in notas:
    if nota > media:
        acima_media += 1
print(f"f) notas acima da média: {acima_media}")

menos_sete = 0
for nota in notas:
    if nota < 7:
        menos_sete += 1
print(f"g) notas abaixo da média: {menos_sete}")

print("h) UHUUUUUU ACABOU EBA!")
