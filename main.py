import pygame
import os
import sys
import time
import threading


def resource_path(relative_path):
    
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


PASTA_MUSICAS = "musicas"
TIPOS_SUPORTADOS = (".mp3",)


pygame.mixer.init()
playlist = []
caminho_da_pasta_musicas = resource_path(PASTA_MUSICAS)

try:
    for arquivo in os.listdir(caminho_da_pasta_musicas):
        if arquivo.lower().endswith(TIPOS_SUPORTADOS):
            playlist.append(arquivo)
except FileNotFoundError:
    print(f"ERRO: A pasta '{PASTA_MUSICAS}' não foi encontrada dentro do executável!")
    time.sleep(5)
    exit()

if not playlist:
    print(f"Nenhuma música foi encontrada na pasta '{PASTA_MUSICAS}'.")
    time.sleep(5)
    exit()

stop_thread = threading.Event()

def aguardar_input_para_parar():
    
    input() 
    stop_thread.set() 


while True:
    os.system("cls" if os.name == "nt" else "clear")
    print("=============================")
    print("      REPRODUTOR DE MÚSICAS")
    print("=============================")
    for indice, musica in enumerate(playlist):
        print(f"{indice + 1}. {musica}")
    print("=============================")
    print("0. Sair do programa")

    try:
        escolha = int(input("\nEscolha uma música pelo número: "))
        if escolha == 0:
            break

        if 1 <= escolha <= len(playlist):
            musica_escolhida = playlist[escolha - 1]
            caminho_completo = os.path.join(caminho_da_pasta_musicas, musica_escolhida)
            
            print(f"\n▶️ Tocando agora: {musica_escolhida}")
            print("\n   Pressione [ENTER] a qualquer momento para parar a música e voltar ao menu.")

            pygame.mixer.music.load(caminho_completo)
            pygame.mixer.music.play()
            
            stop_thread.clear()
            thread_de_input = threading.Thread(target=aguardar_input_para_parar, daemon=True)
            thread_de_input.start()
            
            while pygame.mixer.music.get_busy() and not stop_thread.is_set():
                time.sleep(0.1)

            if stop_thread.is_set():
                pygame.mixer.music.stop()
                print("\n\nMúsica interrompida!")
            else:
                print("\n\nMúsica finalizada!")
            
            print("Pressione Enter para voltar ao menu.")
           
            if not stop_thread.is_set():
                input()

        else:
            print("\nEscolha inválida. Pressione Enter para tentar novamente.")
            input()
            
    except ValueError:
        print("\nEntrada inválida! Por favor, digite um número. Pressione Enter.")
        input()

print("\nObrigado por usar o reprodutor de músicas!")