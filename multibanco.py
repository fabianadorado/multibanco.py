import getpass
import datetime
import os

class multibanco:
    def __init__(self):
       
        self.acesso = {
                "1234": {"nome": "João Silva", "saldo": 1000.0, "movimentos": []},
                "5678": {"nome": "Maria Santos", "saldo": 1000.0, "movimentos": []},
                "0000": {"nome": "Admin Sistema", "saldo": 1000.0, "movimentos": []},
                "9999": {"nome": "Usuário Teste", "saldo": 1000.0, "movimentos": []},
                "1111": {"nome": "Carlos Oliveira", "saldo": 1000.0, "movimentos": []},
                "2222": {"nome": "Ana Costa", "saldo": 1000.0, "movimentos": []}
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
            pin = getpass.getpass("Digite seu PIN")

            if pin in self.acesso:
                self.usuario_logado = pin
                nome = self.acesso[pin]["nome"]
                print(f"Bem-vindo, {nome}")
                input("Pressione Enter para continuar")
                return nome
            else:
                print("PIN incorreto")
                tentativas += 1
        self.limpar_tela()
        print("Número de tentativas excedido. Cartão bloqueado.")
        return None

    def consultar_saldo(self):
        self.limpar_tela()
        pin = self.usuario_logado
        saldo = self.acesso[pin]["saldo"]
        print(f"Saldo atual: {saldo:.2f} €")
        input("Pressione Enter para continuar")
        return saldo
      

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
        