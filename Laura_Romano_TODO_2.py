def calculo(N, z, p, e):
    return round((z**2)*(p*(1-p))/(e**2) / (1 + (z**2)*(p*(1-p))/((e**2)*N)))


N = int(input('Insira a quantidade da população: '))

confianca = int(input(
    'Insira o grau de confiança (80, 85, 90, 95 ou 99): '))

if confianca == 80:
    z = 1.28
elif confianca == 85:
    z = 1.44
elif confianca == 90:
    z = 1.65
elif confianca == 95:
    z = 1.96
elif confianca == 99:
    z = 2.58

e = float(input('Insira a margem de erro em decimais:'))

p = 0.5

print('O valor da amostra deve ser {}'.format(calculo(N, z, p, e)))
