# Programa que a partir do sexo do usuário retorna seu peso ideal
print ('Qual seu peso ideal?')

# Entrada das variáveis
# Requisita ao usuário seu sexo
sexo = input('Digite seu sexo (H/M): ')
# Requisita ao usuário sua altura
altura = eval(input('Digite sua altura em metros: '))

# Aplica a fórmula de acordo com o sexo e dá o retorno do peso ideal
if sexo == 'H':
    peso_ideal_H = (72.7 * altura) - 58
    print (f'Seu peso ideal é ', peso_ideal_H)
else:
    peso_ideal_M = (62.1 * altura) - 44.7
    print (f'Seu peso ideal é ', peso_ideal_M)



