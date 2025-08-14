from tkinter import *
import tkinter as tk
import time
import requests
import random
import os

janela_virus = tk.Tk()             
janela_virus.title("Janela do virus")
janela_virus.geometry("958x720")
janela_virus.configure(bg="darkgreen")
imagem_fundo = tk.PhotoImage(file="warning2.png")
label_fundo = tk.Label(janela_virus, image=imagem_fundo)
label_fundo.place(x=0, y=0, relwidth=1, relheight=1)
tk.Label(janela_virus, text="INSTALANDO VÍRUS MORTAL", fg="#fece00",bg="#060606", font=("Arial", 30, "bold")).pack(anchor="center", pady=250, padx=20)


largura_tela = janela_virus.winfo_screenwidth()
altura_tela = janela_virus.winfo_screenheight()

for i in range(300):
        x = random.randint(0, largura_tela - 400)
        y = random.randint(0, altura_tela - 200)
        nova_janela = tk.Toplevel(janela_virus)
        nova_janela.geometry(f"400x200+{x}+{y}")
        nova_janela.configure(bg="black")
        nova_janela.title(f"Vírus {i+1}")
        tk.Label(nova_janela, text="⚠️ VÍRUS DETECTADO ⚠️", fg="lime", bg="black", font=("Arial", 16, "bold")).pack(expand=True)
        janela_virus.update()
        time.sleep(0.01)

url = "https://www.kaspersky.com.br/content/pt-br/images/repository/isc/2021/what-is-pup.jpg"
nome_arquivo = "INSTALADO.jpg"
resposta = requests.get(url)

if resposta.status_code == 200:
    with open(nome_arquivo, 'wb') as f:
        f.write(resposta.content)
    print(f"Imagem salva como {nome_arquivo}")
    os.startfile(nome_arquivo)
else:
    print("Erro ao baixar a imagem:", resposta.status_code)
