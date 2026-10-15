# RentSmart

O RentSmart é um sistema desenvolvido em Python para calcular o aluguel de imóveis de acordo com suas características. Ele valida os dados informados, calcula o valor do aluguel e da taxa contratual, que pode ser parcelada em até 5 vezes. Ao final, apresenta o orçamento e gera um arquivo CSV com a previsão dos gastos durante 12 meses.

Inicialmente, o programa solicita ao usuário as informações necessárias para realizar o orçamento, como o tipo de imóvel desejado, a quantidade de quartos, as vagas de garagem ou estacionamento e as condições para aplicação de desconto. Também solicita a quantidade de parcelas para o pagamento da taxa contratual.

Após receber as informações, o sistema verifica as opções escolhidas e aplica as regras comerciais de cada imóvel.

Apartamento: aluguel inicial de R$ 700,00, adicional de R$ 200,00 para dois quartos, R$ 300,00 para garagem e desconto de 5% para clientes que informarem não possuir crianças.

Casa: aluguel inicial de R$ 900,00, adicional de R$ 250,00 para dois quartos e R$ 300,00 para garagem.

Estúdio: aluguel inicial de R$ 1.200,00, pacote de duas vagas por R$ 250,00 e adicional de R$ 60,00 por vaga extra.

Além do aluguel, o sistema calcula separadamente a taxa contratual de R$ 2.000,00, que pode ser dividida em até cinco parcelas de R$ 400,00. Dessa forma, o usuário consegue visualizar o valor do aluguel e as condições de pagamento da taxa sem confundir os dois custos.
O projeto utiliza os conceitos de Programação Orientada a Objetos (POO), que permitem organizar o código por meio de classes, objetos, atributos e métodos. Essa organização ajuda a separar as responsabilidades do sistema, facilita a manutenção do código e evita a repetição desnecessária de instruções.  
Depois de realizar os cálculos, o sistema apresenta um resumo detalhado do orçamento, informando o tipo de imóvel, o valor inicial, os adicionais aplicados, os descontos, o aluguel mensal final e os dados da taxa contratual.
Por fim, o programa gera um arquivo CSV com a projeção dos 12 meses da locação. Esse arquivo permite consultar os valores previstos durante o primeiro ano do contrato e visualizar os dados em programas como Microsoft Excel.

