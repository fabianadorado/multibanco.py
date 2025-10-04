import getpass
import datetime
import os
import  sys

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
    
    def submenu(self):
        print("=" *40)
        while True:
            try:
                escolha = input("Deseja realizar outra operação? (s/n): ").strip().lower()
                if escolha in ("s", "sim"):
                    return   # volta ao menu principal
                elif escolha in ("n", "nao", "não"):
                    print("Saindo do programa...")
                    sys.exit(0)
                else:
                    print("Opção inválida. Responda com 's' ou 'n'.")
            except (KeyboardInterrupt, EOFError):
                print("\nInterrupção detectada. Saindo com segurança...")
                sys.exit(0)
            except Exception as e:
                print(f"Ocorreu um erro inesperado: {e}")
    
    def pergunta_outra_transferencia(self):
        escolha = input("Deseja realizar outra transferência? (s/n): ").strip().lower()
        if escolha in ("s", "sim"):
            self.limpar_tela()
            numero_conta = self.usuario_logado
            self.cabecalho("TRANSFERÊNCIA", numero_conta, mostrar_saldo=True)
            print("Digite os dados para transferência.")
            return True  # continuar na transferência
        else:
            self.limpar_tela()
            return False  # voltar ao menu

    def cabecalho(self, titulo, numero_conta=None, mostrar_saldo=False, largura=40, tipo="padrao"):
        
        if tipo == "login":
            print("=" *40)
            print("TERMINAL MULTIBANCO".center(40))
            print("=" *40)
            print("Bem-vindo!".center(40))
            print(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S").center(40))
            print("-" *40)
            print("Por favor, insira seus dados para".center(40))
            print("continuar.".center(40))
            print("-" *40)
        elif tipo == "bemvindo":
            print("=" *45)
            print("TERMINAL MULTIBANCO".center(45))
            print("=" *45)
            print(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S").center(45))
            print(f"\nOlá {self.acesso[numero_conta]['nome']}, seja Bem-vindo!\n".center(50))
            print("-" *45)
        elif tipo == "historico":
            print("=" *largura)
            print(titulo.center(largura))
            print("=" *largura)
            print(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S").center(largura))
            print("=" *largura)
        else:  # padrao
            print("=" *largura)
            print(titulo.center(largura))
            print("=" *largura)
            print(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S").center(largura))
            print("-" *largura)
            
            if mostrar_saldo and numero_conta:
                saldo = self.acesso[numero_conta]["saldo"]
                print(f"Saldo Atual:" + f" € {saldo:.2f}".rjust(25))
                print("=" *largura)
            
  
    def logar(self):
        self.limpar_tela()
        self.cabecalho("", tipo="login")
        tentativas = 0
        while tentativas < 3:

            numero_conta=input("Nº da sua conta: ")
            pin = getpass.getpass("PIN de Acesso: ")

            if numero_conta in self.acesso and self.acesso[numero_conta]["pin"] == pin:

                self.usuario_logado = numero_conta
                conta_encontrada = self.acesso[numero_conta]
                self.limpar_tela()
                self.cabecalho("", numero_conta, tipo="bemvindo")
                input("Pressione Enter e Escolha a opção desejada.")
                
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
        self.cabecalho("SALDO", numero_conta, mostrar_saldo=True)
        self.submenu()
        self.limpar_tela()
        
 
    def realizar_levantamento(self):
        while True:
            self.limpar_tela()
            numero_conta = self.usuario_logado
            self.cabecalho("LEVANTAMENTO", numero_conta, mostrar_saldo=True)
            try:
                valor = float(input("Informe o valor a levantar (€): "))
                print("-" *40)
                if valor <=10:
                    print("\nLimite mínimo de levantamento é de € 10,00")
                    input("Pressione Enter e Escolha outro valor.")
                    continue
                elif valor > self.acesso[numero_conta]["saldo"]:
                    print("\nSaldo Insuficiente")
                    input("Pressione Enter e Escolha outro valor.")
                    continue
                else:
                    self.acesso[numero_conta]["saldo"] -= valor
                    movimento ={
                        "tipo" : "Levantamento",
                        "valor" : -valor,
                        "data" : datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
                        "descricao" : "Levantamento em multibanco"
                    }
                    self.acesso[numero_conta]["movimentos"].append(movimento)
                    print(f"\nLevantamento de € {valor:.2f} Autorizado!")
                    print(f"Saldo Atual:" + f" € {self.acesso[numero_conta]['saldo']:.2f}".rjust(25))
                    print("=" *40)
                    input("\nRetire o seu dinheiro...")
                    self.limpar_tela()  
                    return
                                  

            except ValueError:
                print("\nValor inválido!")
                input("Pressione Enter para voltar ao menu...")
            
            return

    def realizar_deposito(self):
        while True:
            self.limpar_tela()
            numero_conta = self.usuario_logado
            self.cabecalho("DEPÓSITO", numero_conta, mostrar_saldo=True)

            try:
                valor = float(input("Digite o valor a depositar: € "))
                print("-" *40)
                if valor<=0:
                    print["Valor deve ser positivo!"]
                    input("Pressione Enter e Escolha outro valor.")
                    continue
                else:
                    self.acesso[numero_conta]["saldo"] += valor
                    movimento ={
                        "tipo" : "Depósito",
                        "valor" : +valor,
                        "data" : datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
                        "descricao" : "Depósito em multibanco"
                    }
                    self.acesso[numero_conta]["movimentos"].append(movimento)
                    print(f"Depósito realizado com sucesso.")
                    print(f"Saldo Atual:" + f" € {self.acesso[numero_conta]['saldo']:.2f}".rjust(25))
                    print("=" *40)
                    self.submenu()
                    self.limpar_tela()  
            except ValueError:
                print("\nValor inválido!")
                input("\nPressione Enter para voltar ao menu...")
            return

    def realizar_transferencia(self):
        self.limpar_tela()
        numero_conta = self.usuario_logado
        self.cabecalho("TRANSFERÊNCIA", numero_conta, mostrar_saldo=True)
        print("Digite os dados para transferência.")
        while True:
            try:
                conta_destino = input("Conta de destino: ")
                valor = float(input("Valor a transferir: € "))

                if conta_destino not in self.acesso:
                     print("Conta não encontrada!")
                     print("-" *40)
                     if self.pergunta_outra_transferencia():
                         continue
                     else:
                         return
                elif conta_destino == numero_conta:
                     print("Não pode transferir para a própria conta!")
                     print("-" *40)
                     if self.pergunta_outra_transferencia():
                         continue
                     else:
                         return
                elif valor <= 0:
                     print("Valor deve ser positivo e válido!")
                     print("-" *40)
                     if self.pergunta_outra_transferencia():
                         continue
                     else:
                         return
                elif valor > self.acesso[numero_conta]["saldo"]:
                     print("Saldo insuficiente!")
                     print("-" *40)
                     if self.pergunta_outra_transferencia():
                         continue
                     else:
                         return
                else:
                    self.acesso[numero_conta]['saldo'] -= valor
                    self.acesso[conta_destino]['saldo'] += valor

                    movimento_origem = {
                        "tipo": "Transferência",
                        "valor": -valor,
                        "data": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
                        "descricao": f"Transferência para conta {conta_destino}"
                    }
                    movimento_destino = {
                        "tipo": "Transferência",
                        "valor": valor,
                        "data": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
                        "descricao": f"Transferência recebida conta {numero_conta}"
                    }
                    self.acesso[numero_conta]["movimentos"].append(movimento_origem)
                    self.acesso[conta_destino]["movimentos"].append(movimento_destino)
                    print("-" *40)
                    print(f"Transferência de € {valor:.2f} para conta {conta_destino}\ncliente {self.acesso[conta_destino]['nome']} realizada com sucesso!")
                    
                    print(f"Saldo Atual:" + f" € {self.acesso[numero_conta]['saldo']:.2f}".rjust(25))
                    print("=" *40)
                    self.submenu()
                    self.limpar_tela()
                    return  

            except ValueError:
                 print("Valor inválido!") 
                 print("-" *40)
                 self.submenu()
                 return


    def consultar_movimentos(self):
        self.limpar_tela()
        numero_conta = self.usuario_logado
        movimento = self.acesso[numero_conta]["movimentos"]
        
        self.cabecalho("HISTÓRICO DE MOVIMENTOS", largura=55, tipo="historico")

        if not movimento:
            print("Nenhum movimento registado.")
        else:
            ultimos_movimentos = movimento[-10:]
            for i, mov in enumerate(ultimos_movimentos,1):
                print(f"{i:<3} | {mov['data']:<16} | {mov['tipo']:<15} | € {mov['valor']:>5.2f}")
                if mov['descricao']:
                    print(f"Descrição: {mov['descricao']}\n")
                    print("=" *55)
        input("\nPressione Enter para voltar ao menu...")
        self.limpar_tela()


    def menu(self):
        self.limpar_tela()
        while True:
            print("=" *30)
            print("MENU MULTIBANCO".center(30))
            print("=" *30)
            print(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S".center(30)))
            print("-" *30)
            print("1 - Consultar Saldo")
            print("2 - Realizar Levantamento")
            print("3 - Realizar Depósito")
            print("4 - Realizar Transferência")
            print("5 - Consultar Movimentos")
            print("6 - Acessar Outra Conta")
            print("7 - Sair")
            print("=" *30)
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
                    self.logar()
                case "7":
                    print("Obrigado por usar o Multibanco")
                    break
                case _:
                    print("Opção inválida")

from multibanco import multibanco

if __name__ == "__main__": 
    app = multibanco()
    if app.logar():
        app.menu() 
        
    else:
        print("Encerrando Sistema.")