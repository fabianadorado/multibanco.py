# multibanco.py
Simulador Multibanco em Python

Enunciado: Simulação de um Mulibanco de um Banco
Descrição do Problema: Crie um programa em Python que simule o funcionamento de um
multibanco de um banco simples. O sistema deve permitir que o utilizador realize operações
básicas de gestão de conta bancária, como consultas, levantamentos, depósitos e
transferências. Além disso, o programa deve registar todos os movimentos (transações)
realizados e fornecer estatisticas básicas sobre a atividade da conta. O programa deve ser
interativo, utilizando um menu de opções exibido no terminal, e deve validar as entradas do
utilizador para evitar erros (por exemplo, levantamentos acima do saldo). 

Para simplificar, Armazene os dados da conta (incluindo histórico de movimentos) em variáveis ou numa
estrutura simples como um dicionário ou lista. O programa deve con􀆟nuar a funcionar até que
o utilizador escolha sair.
Requisitos Gerais:
- Utilize estruturas de controlo como if-elif-else, ciclos (while) e funções para
modularizar o código.
- Trate exceções básicas (ex.: entrada inválida com try-except).
- Validações
- Exiba mensagens claras em português para o utilizador.
- O saldo inicial da conta deve ser definido como € 1000,00.
- Mantenha um registo de movimentos numa lista de dicionários, onde cada movimento
inclui: Tipo (ex.: "Depósito", "Levantamento", "Transferência"), valor, data/hora
aproximada (use datetime para timestamp) e descrição breve (ex.: para transferências,
inclua o número da conta destino).
Funcionalidades Principais a Implementar:

1. Código Pin - Um Pin de 4 dígitos
2. Exibir Menu Principal U􀆟lizador:
3. Mostre um menu com opções numeradas:
  1. Consultar Saldo
  2. Realizar Levantamento
  3. Realizar Depósito
  4. Realizar Transferência
  5. Consultar Movimentos
  6. Sair
     
Leia a opção do utilizador e chame a função correspondente.
4. Consultar Saldo:
- Exiba o saldo atual da conta formatado como moeda (ex.: "Saldo atual: €
1.000,00").
5. Realizar Levantamento:
- Peça o valor a levantar (deve ser um número posi􀆟vo).
- Verifique se o valor é menor ou igual ao saldo disponível.
- Se sim, subtraia do saldo, registe o movimento na lista de histórico e confirme
a operação; caso contrário, exiba uma mensagem de erro (ex.: "Saldo
insuficiente").
- Considere um limite mínimo de levantamento (ex.: € 10,00).
6. Realizar Depósito:
- Peça o valor a depositar (deve ser um número posi􀆟vo).
- Adicione ao saldo, registe o movimento na lista de histórico e confirme a
operação.
- Exiba o novo saldo.
7. Realizar Transferência:
- Peça o valor a transferir e o número da conta de destino (simule como uma
string simples).
- Verifique se o valor é menor ou igual ao saldo.
- Se sim, subtraia do saldo atual, registe o movimento na lista de histórico e
exiba uma mensagem de confirmação (ex.: "Transferência de € 100,00 para a
conta 12345 realizada com sucesso").
- Caso contrário, exiba erro de saldo insuficiente.
8. Consultar Movimentos:
- Exiba uma lista dos úl􀆟mos 10 movimentos (ou todos se houver menos),
formatados de forma legível (ex.: "2025-10-01 14:30 - Depósito: € 200,00").
- Inclua Tipo, valor, data/hora e descrição.
- Se não houver movimentos, exiba "Nenhum movimento registado."
-Retorne ao menu principal.

9. Sair do Sistema:
 -Exiba uma mensagem de despedida (ex.: "Obrigado por usar o Multibanco.
Volte sempre!") e termine o programa.
