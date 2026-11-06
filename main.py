import tkinter as tk
import customtkinter as ctk


ctk.set_appearance_mode("light")  
ctk.set_default_color_theme("blue")

janela = ctk.CTk()
janela.title("Fiap - amais")
janela.geometry("1440x900")
janela.configure(fg_color="#FFFBFB")


esclero_estado = {"oculto": True}

def alternar_senha():
    if esclero_estado["oculto"]:
        campo_senha.configure(show="")  
        botao_olho.configure(text="🙈")
        esclero_estado["oculto"] = False
    else:
        campo_senha.configure(show="*")  
        botao_olho.configure(text="👁️")
        esclero_estado["oculto"] = True



imagem_original = tk.PhotoImage(file="image 1.png")
imagem_tk = imagem_original.subsample(1, 1) 

label_logo = tk.Label(janela, image=imagem_tk, bg="#FFFBFB")
label_logo.place(relx=0.5, y=220, anchor="center") 



campo_email = ctk.CTkEntry(
    janela, 
    placeholder_text="E-mail", 
    width=440, 
    height=55, 
    font=("Arial", 16),
    fg_color="white", 
    text_color="black",
    placeholder_text_color="#A0A0A0",
    border_color="#A0A0A0",
    border_width=1,
    corner_radius=4  
)
campo_email.place(relx=0.5, y=390, anchor="center")



campo_senha = ctk.CTkEntry(
    janela, 
    placeholder_text="Senha", 
    show="*",
    width=440, 
    height=55, 
    font=("Arial", 16),
    fg_color="white", 
    text_color="black",
    placeholder_text_color="#A0A0A0",
    border_color="#A0A0A0",
    border_width=1,
    corner_radius=4
)
campo_senha.place(relx=0.5, y=480, anchor="center")


botao_olho = ctk.CTkButton(
    janela, 
    text="👁️", 
    font=("Arial", 16),
    width=30,
    height=30,
    fg_color="white", 
    text_color="black",
    hover_color="#F0F0F0",
    command=alternar_senha
)
botao_olho.place(x=910, y=480, anchor="center")



botao_entrar = ctk.CTkButton(
    janela, 
    text="ACESSAR", 
    font=("Arial", 14, "bold"), 
    fg_color="#0084C9", 
    text_color="white", 
    hover_color="#006fa8",
    width=440, 
    height=50,
    corner_radius=4
)
botao_entrar.place(relx=0.5, y=570, anchor="center")



botao_primeiro_acesso = ctk.CTkLabel(
    janela, 
    text="PRIMEIRO ACESSO?", 
    font=("Arial", 12, "bold"), 
    text_color="#0084C9",
    cursor="hand2"
)
botao_primeiro_acesso.place(relx=0.5, y=630, anchor="center")


janela.mainloop()