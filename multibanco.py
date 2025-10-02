import getpass
import datetime
import os

class multibanco:
    def __init__(self):
       
        self.acesso = {
            "1001": {"nome": "João Silva", "pin": "1234", "saldo": 1000.0, "movimentos": []},
            "1002": {"nome": "Maria Santos", "pin": "5678", "saldo": 1000.0, "movimentos": []},
            "1003": {"nome": "Admin Sistema", "pin": "0000", "saldo": 1000.0, "movimentos": []},
            "1004": {"nome": "Usuário Teste", "pin": "9999", "saldo": 1000.0, "movimentos": []},
            "1005": {"nome": "Carlos Oliveira", "pin": "1111", "saldo": 1000.0, "movimentos": []},
            "1006": {"nome": "Ana Costa", "pin": "2222", "saldo": 1000.0, "movimentos": []}
            }
        self.usuario_logado = None

    def limpar_tela(self):
        os.system("cls" if os.name == "nt" else "clear")
    
      
    def logar(self):
        self.limpar_tela()
        print("*" *40)
        print("Bem-vindo ao Multibanco")
        print("*" *40)

        tentativas = 0
        while tentativas < 3:

            numero_conta=input("Digite o nº da sua conta: ")
            pin = getpass.getpass("Digite seu PIN: ")

            if numero_conta in self.acesso and self.acesso[numero_conta]["pin"] == pin:

                self.usuario_logado = numero_conta
                conta_encontrada = self.acesso[numero_conta]
                print(f"Bem-vindo, {conta_encontrada['nome']}")
                input("Pressione Enter para continuar")
                return conta_encontrada
            else:
                print("PIN incorreto")
                tentativas += 1
        self.limpar_tela()
        print("Número de tentativas excedido. Cartão bloqueado.")
        return None

    def consultar_saldo(self):
        self.limpar_tela()
        numero_conta = self.usuario_logado
        saldo = self.acesso[numero_conta]["saldo"]
        print("=" *20)
        print(" SALDO ")
        print("=" *20)
        print(f"Saldo atual: € {saldo:.2f} ")
        input("Pressione Enter para continuar")
        self.limpar_tela()
        return saldo
     
    def realizar_levantamento(self):
        self.limpar_tela()
        numero_conta = self.usuario_logado
        saldo = self.acesso[numero_conta]["saldo"]
        print("=" *20)
        print(" LEVANTAMENTO ")
        print("=" *20)
        print(f"Saldo atual: € {saldo:.2f} ")
        try:
            valor = float(input("Digite o valor a levantar: € "))
            if valor > saldo:
                print("Saldo insuficiente")
                input("Pressione Enter para continuar")
            else:
                self.acesso[numero_conta]["saldo"] -= valor
                movimento ={
                    "tipo" : "Levantamento",
                    "valor" : -valor,
                    "data" : datetime.now().strftime("%Y-%m-%d %H:%M"),
                    "descricao" : "Levantamento em multibanco"
                }
                self.acesso[numero_conta]["movimentos"].append[movimento]
                print(f"Levantamento de € {valor:.2f}  realizado com sucesso")

        except ValueError:
            print["Valor inválido!"]

        input("Pressione Enter para continuar")
        self.limpar_tela()
        self.consultar_saldo()  
        return

    def realizar_deposito(self):
        self.limpar_tela()

        numero_conta = self.usuario_logado
        print("=" *20)
        print(" DEPÓSITO ")
        print("=" *20)

        try:
            valor = float(input("Digite o valor a depositar: € "))
            if valor<=0:
                print["Valor deve ser positivo!"]
            else:
                self.acesso[numero_conta]["saldo"] -= valor
                movimento ={
                    "tipo" : "Depósito",
                    "valor" : valor,
                    "data" : datetime.now().strftime("%Y-%m-%d %H:%M"),
                    "descricao" : "Depósito em multibanco"
                }
                self.acesso[numero_conta]["movimentos"].append[movimento]
                print(f"Depósito de € {valor:.2f}  realizado com sucesso")

        except ValueError:
            print["Valor inválido!"]

        input("Pressione Enter para continuar")
        self.limpar_tela()
        self.consultar_saldo()  
        return

    def realizar_transferencia(self):
        self.limpar_tela()

        numero_conta = self.usuario_logado
        saldo = self.acesso[numero_conta]["saldo"]
        print("=" *20)
        print(" TRANSFERÊNCIA ")
        print("=" *20)
        print(f"Saldo atual: € {saldo:.2f} ")
        print("Digite os dados para transferência.")

        try:
            conta_destino = input("Conta de destino: ")
            valor = float(input("Valor a transferir: € "))

            if conta_destino not in self.acesso:
                print("Conta não encontrada!")
            elif conta_destino == numero_conta:
                print("Não pode transferir para a própria conta!")
            elif valor <= 0:
                print("Valor deve ser positivo e válido!")
            elif valor > saldo:
                print("Saldo insuficiente!")
            else:
                self.acesso[numero_conta]['saldo'] -= valor
                self.acesso[conta_destino]['saldo'] += valor

                movimento_origem = {
                    "tipo": "Transferência",
                    "valor": -valor,
                    "data": datetime.now().strftime("%Y-%m-%d %H:%M"),
                    "descricao": f"Transferência para conta {conta_destino}"
                }
                movimento_destino = {
                    "tipo": "Transferência",
                    "valor": valor,
                    "data": datetime.now().strftime("%Y-%m-%d %H:%M"),
                    "descricao": f"Transferência para conta {numero_conta}"
                }
                self.acesso[numero_conta]["movimentos"].append(movimento_origem)
                self.acesso[conta_destino]["movimentos"].append(movimento_destino)
                
                print(f"Transferência de € {valor:.2f} realizada com sucesso!")
                print(f"Novo saldo: € {self.acesso[numero_conta]['saldo']:.2f}")
        
        except ValueError:
            print(" Valor inválido!") 
        input("\nPressione Enter para voltar ao menu...")

    def consultar_movimentos(self):
        self.limpar_tela()
        numero_conta = self.usuario_logado
        movimento = self.acesso[numero_conta]["movimentos"]
        print("=" *20)
        print(" HISTÓRICO MOVIMENTAÇÃO ")
        print("=" *20)

        if not movimento:
            print("Nenhum movimento registado.")
        else:
            ultimos_movimentos = movimento[-10:]
            for i, mov in enumerate(ultimos_movimentos,1):
                print(f"{i} - {mov['data']} - {mov['tipo']}: € {mov['valor']: 2f}")
                if mov['descricao']:
                    print(f"    Drescrição: {mov['descricao']}")
        input("\nPressione Enter para voltar ao menu...")
        self.limpar_tela()


    def menu(self):
        self.limpar_tela()
        while True:
            print("\n=== MENU MULTIBANCO ===")
            print("1 - Consultar Saldo")
            print("2 - Realizar Levantamento")
            print("3 - Realizar Depósito")
            print("4 - Realizar Transferência")
            print("5 - Consultar Movimentos")
            print("6 - Sair")
            opcao = input("Escolha uma opção: ").strip()
            match opcao:
                case "1":
                    self.consultar_saldo()
                case "2":
                    self.realizar_levantamento()
                case "3":
                    self.realizar_deposito()
                case "4":
                    self.realizar_transferencia()
                case "5":
                    self.consultar_movimentos()
                case "6":
                    print("Obrigado por usar o Multibanco")
                    break
                case _:
                    print("Opção inválida")
        