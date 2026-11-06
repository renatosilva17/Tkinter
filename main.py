import tkinter as tk

janela = tk.Tk()
janela.title("Fiap - amais")
janela.geometry("1440x900")
janela.configure(bg="#FFFBFB")

imagem = tk.PhotoImage(file="image 1.png")
label_imagem = tk.Label(janela, image=imagem, bg="#FFFBFB")
label_imagem.pack(pady=20)
janela.mainloop()