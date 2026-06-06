# Programa que verifica se um número é Primo
# Um número é considerado primo se ele é divisível somente por dois números (ele mesmo e 1)


print("Programa de verificação de número PRIMO")

# Usuario digita o número a ser testado
numero_digitado = int(input("Digite um número: "))

# Definição das variáveis
x = 1
contador = 0

# Fazer o loop de dividir o número proposto por todos os números, começando em 1, até chegar ao valor dele mesmo
while x <= numero_digitado:
    if numero_digitado % x == 0:
        contador += 1
    x += 1

if contador == 2:
    print("É primo")
else:
    print("Não é primo")

