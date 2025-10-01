# multibanco.py
Simulador Multibanco em Python

Enunciado: Simulação de um Mul􀆟banco de um Banco
Descrição do Problema: Crie um programa em Python que simule o funcionamento de um
mul􀆟banco de um banco simples. O sistema deve permi􀆟r que o u􀆟lizador realize operações
básicas de gestão de conta bancária, como consultas, levantamentos, depósitos e
transferências. Além disso, o programa deve registar todos os movimentos (transações)
realizados e fornecer esta􀆡s􀆟cas básicas sobre a a􀆟vidade da conta. O programa deve ser
intera􀆟vo, u􀆟lizando um menu de opções exibido no terminal, e deve validar as entradas do
u􀆟lizador para evitar erros (por exemplo, levantamentos acima do saldo). Para simplificar,
Armazene os dados da conta (incluindo histórico de movimentos) em variáveis ou numa
estrutura simples como um dicionário ou lista. O programa deve con􀆟nuar a funcionar até que
o u􀆟lizador escolha sair.
Requisitos Gerais:
 U􀆟lize estruturas de controlo como if-elif-else, ciclos (while) e funções para
modularizar o código.
 Trate exceções básicas (ex.: entrada inválida com try-except).
 Validações
 Exiba mensagens claras em português para o u􀆟lizador.
 O saldo inicial da conta deve ser definido como € 1000,00.
 Mantenha um registo de movimentos numa lista de dicionários, onde cada movimento
inclui: 􀆟po (ex.: "Depósito", "Levantamento", "Transferência"), valor, data/hora
aproximada (use date􀆟me para 􀆟mestamp) e descrição breve (ex.: para transferências,
inclua o número da conta des􀆟no).
Funcionalidades Principais a Implementar:
1. Código Pin
o Um Pin de 4 dígitos
2. Exibir Menu Principal U􀆟lizador:
o Mostre um menu com opções numeradas:
1. Consultar Saldo
2. Realizar Levantamento
3. Realizar Depósito
4. Realizar Transferência
5. Consultar Movimentos
6. Sair
o Leia a opção do u􀆟lizador e chame a função correspondente.
3. Consultar Saldo:
o Exiba o saldo atual da conta formatado como moeda (ex.: "Saldo atual: €
1.000,00").
4. Realizar Levantamento:
o Peça o valor a levantar (deve ser um número posi􀆟vo).
o Verifique se o valor é menor ou igual ao saldo disponível.
o Se sim, subtraia do saldo, registe o movimento na lista de histórico e confirme
a operação; caso contrário, exiba uma mensagem de erro (ex.: "Saldo
insuficiente").
o Considere um limite mínimo de levantamento (ex.: € 10,00).
5. Realizar Depósito:
o Peça o valor a depositar (deve ser um número posi􀆟vo).
o Adicione ao saldo, registe o movimento na lista de histórico e confirme a
operação.
o Exiba o novo saldo.
6. Realizar Transferência:
o Peça o valor a transferir e o número da conta de des􀆟no (simule como uma
string simples).
o Verifique se o valor é menor ou igual ao saldo.
o Se sim, subtraia do saldo atual, registe o movimento na lista de histórico e
exiba uma mensagem de confirmação (ex.: "Transferência de € 100,00 para a
conta 12345 realizada com sucesso").
o Caso contrário, exiba erro de saldo insuficiente.
7. Consultar Movimentos:
o Exiba uma lista dos úl􀆟mos 10 movimentos (ou todos se houver menos),
formatados de forma legível (ex.: "2025-10-01 14:30 - Depósito: € 200,00").
o Inclua 􀆟po, valor, data/hora e descrição.
o Se não houver movimentos, exiba "Nenhum movimento registado."
o Retorne ao menu principal.
o
8. Sair do Sistema:
o Exiba uma mensagem de despedida (ex.: "Obrigado por usar o Mul􀆟banco.
Volte sempre!") e termine o programa.
