import getpass
import datetime
import os
import sys
import time
import msvcrt


def input_timeout(prompt: str, timeout: float = 3.0):
    """
    Lê a entrada do utilizador com timeout (segundos).
    - Retorna a string digitada ao pressionar Enter.
    - Retorna None se o timeout expirar sem Enter.
    Observação: funciona em Windows (msvcrt). Em Linux/Mac é preciso outra abordagem.
    """
    if msvcrt is None:
        # Fallback simples: sem timeout (comportamento normal)
        return input(prompt)

    print(prompt, end="", flush=True)
    start = time.time()
    buffer = ""

    while True:
        # se tecla pressionada
        if msvcrt.kbhit():
            ch = msvcrt.getwch()  # wide char
            # Ignorar prefixos de teclas especiais (arrow, função)
            if ch in ("\x00", "\xe0"):
                # tecla especial: ler o segundo código e ignorar
                _ = msvcrt.getwch()
                continue

            # Enter
            if ch == "\r":
                print()  # nova linha
                return buffer

            # Backspace
            if ch == "\x08":
                if len(buffer) > 0:
                    buffer = buffer[:-1]
                    # apagar char na consola
                    sys.stdout.write("\b \b")
                    sys.stdout.flush()
                continue

            # Ctrl+C
            if ch == "\x03":
                raise KeyboardInterrupt

            # Caracter normal -> acrescentar ao buffer e escrever
            buffer += ch
            sys.stdout.write(ch)
            sys.stdout.flush()

        # verificar timeout
        if (time.time() - start) > timeout:
            # imprime linha vazia para não ficar o prompt em alto
            print()
            return None

        # pequeno sleep para não consumir CPU
        time.sleep(0.02)


class Multibanco:
    def __init__(self, timeout_menu: float = 3.0):
        self.acesso = {
            "1001": {"nome": "João Silva", "pin": "1234", "saldo": 1000.0, "movimentos": []},
            "1002": {"nome": "Maria Santos", "pin": "5678", "saldo": 1000.0, "movimentos": []},
            "1003": {"nome": "Admin Sistema", "pin": "0000", "saldo": 1000.0, "movimentos": []},
            "1004": {"nome": "Usuário Teste", "pin": "9999", "saldo": 1000.0, "movimentos": []},
            "1005": {"nome": "Carlos Oliveira", "pin": "1111", "saldo": 1000.0, "movimentos": []},
            "1006": {"nome": "Ana Costa", "pin": "2222", "saldo": 1000.0, "movimentos": []}
        }
        self.usuario_logado = None
        self.timeout_menu = timeout_menu  # segundos para expirar no menu

    def limpar_tela(self):
        os.system("cls" if os.name == "nt" else "clear")

    def cabecalho(self, titulo, numero_conta=None, mostrar_saldo=False, largura=40, tipo="padrao"):
        if tipo == "login":
            print("=" * largura)
            print("TERMINAL MULTIBANCO".center(largura))
            print("=" * largura)
            print("Bem-vindo!".center(largura))
            print(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S").center(largura))
            print("-" * largura)
            print("Por favor, insira seus dados para".center(largura))
            print("continuar.".center(largura))
            print("-" * largura)
        elif tipo == "bemvindo":
            print("=" * largura)
            print("TERMINAL MULTIBANCO".center(largura))
            print("=" * largura)
            print(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S").center(largura))
            print(f"\nOlá {self.acesso[numero_conta]['nome']}, seja Bem-vindo!\n".center(largura))
            print("-" * largura)
        else:
            print("=" * largura)
            print(titulo.center(largura))
            print("=" * largura)
            print(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S").center(largura))
            print("-" * largura)
            if mostrar_saldo and numero_conta:
                saldo = self.acesso[numero_conta]["saldo"]
                print(f"Saldo Atual:" + f" € {saldo:.2f}".rjust(25))
                print("=" * largura)

    def logar(self):
        self.limpar_tela()
        self.cabecalho("", tipo="login")
        tentativas = 0
        while tentativas < 3:
            numero_conta = input("Nº da sua conta: ").strip()
            pin = getpass.getpass("PIN de Acesso: ").strip()

            if numero_conta in self.acesso and self.acesso[numero_conta]["pin"] == pin:
                self.usuario_logado = numero_conta
                self.limpar_tela()
                self.cabecalho("", numero_conta, tipo="bemvindo")
                input("Pressione Enter para continuar...")
                return True
            else:
                print("Nº conta ou PIN incorreto.")
                tentativas += 1

        self.limpar_tela()
        print("Número de tentativas excedido. Cartão bloqueado.")
        return False

    def consultar_saldo(self):
        self.limpar_tela()
        numero = self.usuario_logado
        self.cabecalho("SALDO", numero, mostrar_saldo=True)
        input("\nPressione Enter para voltar ao menu...")

    def realizar_levantamento(self):
        self.limpar_tela()
        numero = self.usuario_logado
        self.cabecalho("LEVANTAMENTO", numero, mostrar_saldo=True)
        texto = input("Informe o valor a levantar (€): ")
        try:
            valor = float(texto.replace(",", "."))
        except Exception:
            print("Valor inválido.")
            input("Pressione Enter para voltar...")
            return
        if valor < 10:
            print("Limite mínimo de levantamento: € 10,00")
            input("Pressione Enter para voltar...")
            return
        if valor > self.acesso[numero]["saldo"]:
            print("Saldo insuficiente.")
            input("Pressione Enter para voltar...")
            return
        self.acesso[numero]["saldo"] -= valor
        mov = {"tipo": "Levantamento", "valor": -valor,
               "data": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
               "descricao": "Levantamento em multibanco"}
        self.acesso[numero]["movimentos"].append(mov)
        print(f"Levantamento de € {valor:.2f} efetuado.")
        input("Pressione Enter para voltar...")

    def realizar_deposito(self):
        self.limpar_tela()
        numero = self.usuario_logado
        self.cabecalho("DEPÓSITO", numero, mostrar_saldo=True)
        texto = input("Digite o valor a depositar: € ")
        try:
            valor = float(texto.replace(",", "."))
        except Exception:
            print("Valor inválido.")
            input("Pressione Enter para voltar...")
            return
        if valor <= 0:
            print("Valor deve ser positivo.")
            input("Pressione Enter para voltar...")
            return
        self.acesso[numero]["saldo"] += valor
        mov = {"tipo": "Depósito", "valor": valor,
               "data": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
               "descricao": "Depósito em multibanco"}
        self.acesso[numero]["movimentos"].append(mov)
        print("Depósito realizado com sucesso.")
        input("Pressione Enter para voltar...")

    def realizar_transferencia(self):
        self.limpar_tela()
        numero = self.usuario_logado
        self.cabecalho("TRANSFERÊNCIA", numero, mostrar_saldo=True)
        conta_destino = input("Conta de destino: ").strip()
        if conta_destino == numero:
            print("Não pode transferir para a própria conta.")
            input("Pressione Enter para voltar...")
            return
        if conta_destino not in self.acesso:
            print("Conta destino não encontrada.")
            input("Pressione Enter para voltar...")
            return
        texto = input("Valor a transferir: € ")
        try:
            valor = float(texto.replace(",", "."))
        except Exception:
            print("Valor inválido.")
            input("Pressione Enter para voltar...")
            return
        if valor <= 0:
            print("Valor deve ser positivo.")
            input("Pressione Enter para voltar...")
            return
        if valor > self.acesso[numero]["saldo"]:
            print("Saldo insuficiente.")
            input("Pressione Enter para voltar...")
            return
        self.acesso[numero]["saldo"] -= valor
        self.acesso[conta_destino]["saldo"] += valor
        mov_origem = {"tipo": "Transferência", "valor": -valor,
                      "data": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
                      "descricao": f"Para conta {conta_destino}"}
        mov_dest = {"tipo": "Transferência", "valor": valor,
                    "data": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
                    "descricao": f"De {numero}"}
        self.acesso[numero]["movimentos"].append(mov_origem)
        self.acesso[conta_destino]["movimentos"].append(mov_dest)
        print(f"Transferência de € {valor:.2f} para conta {conta_destino} realizada.")
        input("Pressione Enter para voltar...")

    def consultar_movimentos(self):
        self.limpar_tela()
        numero = self.usuario_logado
        movs = self.acesso[numero]["movimentos"]
        self.cabecalho("HISTÓRICO DE MOVIMENTOS", largura=55, tipo="historico", numero_conta=numero)
        if not movs:
            print("Nenhum movimento registado.")
        else:
            ultimos = movs[-10:]
            for i, mov in enumerate(ultimos, 1):
                print(f"{i:<3} | {mov['data']:<16} | {mov['tipo']:<15} | € {mov['valor']:>7.2f}")
                if mov.get("descricao"):
                    print(f"    {mov['descricao']}")
                print("-" * 55)
        input("\nPressione Enter para voltar ao menu...")

    def menu(self):
        # Menu com timeout para escolha (volta ao login se expirar)
        while True:
            self.limpar_tela()
            largura = 30
            print("=" * largura)
            print("MENU MULTIBANCO".center(largura))
            print("=" * largura)
            print(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S").center(largura))
            print("-" * largura)
            print("1 - Consultar Saldo")
            print("2 - Realizar Levantamento")
            print("3 - Realizar Depósito")
            print("4 - Realizar Transferência")
            print("5 - Consultar Movimentos")
            print("6 - Sair")
            print("=" * largura)

            opcao = input_timeout("Escolha uma opção: ", timeout=self.timeout_menu)
            if opcao is None:  # timeout expirou -> volta para login (main loop)
                print("Tempo esgotado no menu. Voltando para o login...")
                time.sleep(1.0)
                return

            opcao = opcao.strip()

            # Usando if/elif por compatibilidade com versões <3.10;
            # se tens Python 3.10+, podes substituir por match/case.
            if opcao == "1":
                self.consultar_saldo()
            elif opcao == "2":
                self.realizar_levantamento()
            elif opcao == "3":
                self.realizar_deposito()
            elif opcao == "4":
                self.realizar_transferencia()
            elif opcao == "5":
                self.consultar_movimentos()
            elif opcao == "6":
                print("Obrigado por usar o Multibanco!")
                sys.exit(0)
            else:
                print("Opção inválida.")
                time.sleep(0.8)


if __name__ == "__main__":
    app = Multibanco(timeout_menu=3.0)  # timeout menu em segundos
    while True:
        if app.logar():
            app.menu()
        else:
            print("Encerrando sistema.")
            break