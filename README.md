# Excesso-de-velocidade
Esse é um pequeno programa em Python que solicita ao usuário a velocidade atual de um carro, e então verifica se o carro está acima da velocidade limite de 80 km/h. Se estiver acima, o programa calcula o valor da multa que deve ser paga pelo motorista.

Aqui está uma explicação linha por linha:

velocidade = float(input('Qual a velocidade atual do carro? '))

Essa linha pede ao usuário para inserir a velocidade atual do carro. A função input é usada para ler a entrada do usuário como uma string, que é então convertida em um número decimal de ponto flutuante (float) usando a função float. O valor da velocidade é armazenado na variável velocidade.
multa = (velocidade - 80) * 7

Essa linha calcula o valor da multa que o motorista deve pagar caso esteja acima da velocidade permitida. A fórmula usada para calcular a multa é (velocidade - 80) * 7, o que significa que a multa é calculada como a diferença entre a velocidade atual do carro e o limite de velocidade permitido (que é 80 km/h) multiplicada por 7 (o valor da multa por km/h excedido).
if velocidade > 80:

Essa linha verifica se a velocidade atual do carro é maior do que o limite de velocidade permitido de 80 km/h. Se for verdade, o bloco de código abaixo desta linha é executado. Caso contrário, o programa passa diretamente para a linha 5.
print('MULTADO! Você excedeu o limite de velocidade permitido que é de 80 Km/h. Você deve pagar uma multa de R$ {:.2f}'.format(multa))

Se a velocidade do carro for maior que 80 km/h, esta linha é executada, imprimindo uma mensagem de que o motorista foi multado e o valor da multa que ele deve pagar. A mensagem usa a função format para incluir o valor da multa calculado anteriormente na mensagem. A opção :.2f é usada para formatar o valor da multa como um número decimal com 2 casas decimais.
else:

Se a velocidade do carro não for maior que 80 km/h, esta linha é executada. Isso significa que o motorista não foi multado e o programa passa diretamente para a próxima linha.
print('Tenha um bom dia! Dirija com segurança!')

Essa linha é executada se a velocidade do carro for menor ou igual a 80 km/h. Ela imprime uma mensagem desejando ao motorista um bom dia e lembrando-o de dirigir com segurança.
