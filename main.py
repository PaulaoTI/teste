import tkinter as tk
from tkinter import messagebox

def exibir_mensagem():
    mensagem = entrada.get()
    messagebox.showinfo("Mensagem", f"Você digitou: {mensagem}")

# Criação da janela principal
janela = tk.Tk()
janela.title("Interface Gráfica Simples")

# Configurações da janela
janela.geometry("300x200")  # Largura x Altura

# Label (texto fixo)
label = tk.Label(janela, text="Digite algo:", font=("Arial", 12))
label.pack(pady=10)  # Adiciona ao layout com margem superior/inferior

# Campo de entrada de texto
entrada = tk.Entry(janela, font=("Arial", 12))
entrada.pack(pady=10)

# Botão
botao = tk.Button(janela, text="Exibir Mensagem", command=exibir_mensagem)
botao.pack(pady=10)

# Inicia o loop da interface gráfica
janela.mainloop()
