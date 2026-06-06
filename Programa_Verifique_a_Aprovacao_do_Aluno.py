# Programa que verifica a aprovação de um aluno baseado em duas notas de prova
# n1 tem peso 40% e n2 tem peso 60% e a média para passar é 5.0
print('Verifique sua aprovação')

# Entrada de dados
n1 = eval(input('Digite a sua nota na Prova intermediária (0-10): '))
n2 = eval(input('Digite a sua nota na Prova final(0-10): '))

# Cálculo da média final
media_final = ((n1*0.4) + (n2*0.6))
# Saída de dados
if media_final >= 5:
    print('Parabéns, você foi aprovado!')
else:
    print('Você não alcançou a média necessária para aprovação')



