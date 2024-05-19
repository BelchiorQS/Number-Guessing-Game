import random
import tkinter as tk
from tkinter import messagebox, simpledialog, ttk

def jogo():
    def verificar_palpite():
        palpite = int(entry.get())
        entry.delete(0, 'end')
        nonlocal tentativas
        if palpite == numero_secreto:
            messagebox.showinfo("Resultado", "Parabéns! Você acertou o número secreto.")
            window.quit()
        elif palpite < numero_secreto:
            resultado.set("O número secreto é maior. Tente novamente.")
        else:
            resultado.set("O número secreto é menor. Tente novamente.")
        tentativas -= 1
        tentativas_restantes.set(f"Você tem {tentativas} tentativas restantes.")
        if tentativas == 0:
            messagebox.showinfo("Resultado", "Fim do jogo.")
            window.quit()

    window = tk.Tk()
    window.title("Jogo de Adivinhação")

    # Centralizar a janela
    window_width = 500
    window_height = 500
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    window.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

    tab_control = ttk.Notebook(window)

    tab1 = ttk.Frame(tab_control)
    tab_control.add(tab1, text='Jogo')

    tab2 = ttk.Frame(tab_control)
    tab_control.add(tab2, text='Configurações')

    tab_control.pack(expand=1, fill='both')

    nome = simpledialog.askstring("Entrada", "Por favor, digite o seu nome:")
    dificuldade = simpledialog.askstring("Entrada", "Escolha a dificuldade do jogo (fácil, médio, difícil):")
    if dificuldade.lower() == 'fácil':
        tentativas = 10
        numero_secreto = random.randint(1, 10)
    elif dificuldade.lower() == 'médio':
        tentativas = 7
        numero_secreto = random.randint(1, 20)
    else:
        tentativas = 5
        numero_secreto = random.randint(1, 50)

    tentativas_restantes = tk.StringVar(window, f"Você tem {tentativas} tentativas para adivinhar o número secreto.")
    tk.Label(tab1, textvariable=tentativas_restantes).pack()

    resultado = tk.StringVar(window)
    tk.Label(tab1, textvariable=resultado).pack()

    entry = tk.Entry(tab1)
    entry.pack()

    tk.Button(tab1, text="Verificar Palpite", command=verificar_palpite).pack()

    window.mainloop()

jogo()
