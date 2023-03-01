velocidade = float(input('Qual a velocidade atual do carro? '))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print('MULTADO! Você excedeu o limite de velocidade permitido que é de 80 Km/h Você deve pagar uma multa de R$ {:.2f}'.format(multa))
else:
    print('Tenha um bom dia! Dirija com segurança!')
