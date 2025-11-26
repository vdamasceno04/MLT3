import customtkinter as ctk

def getSentence() -> str:
    # Variável que vai guardar o que o usuário digitar no final
    texto_digitado = ""
    
    # Deixar bonitão com tema escuro (Dark Mode pra parecer hacker)
    ctk.set_appearance_mode("Dark")  
    ctk.set_default_color_theme("blue") 

    janela = ctk.CTk() 
    janela.title("Host A - Digita aí")
    
    # Centralizar a janela no monitor (código padrão de centralizar)
    largura, altura = 500, 350
    larg_tela, alt_tela = janela.winfo_screenwidth(), janela.winfo_screenheight()
    pos_x, pos_y = (larg_tela/2) - (largura/2), (alt_tela/2) - (altura/2)
    janela.geometry('%dx%d+%d+%d' % (largura, altura, pos_x, pos_y))
    
    # Força a janela a ficar na frente de tudo pra não perder ela
    janela.attributes("-topmost", True)

    def quando_clicar_enviar():
        nonlocal texto_digitado
        # Pega do começo (1.0) até o fim (-1c pra tirar a quebra de linha extra)
        texto_digitado = caixa_texto.get("1.0", "end-1c")
        janela.destroy()

    rotulo = ctk.CTkLabel(janela, text="Manda a mensagem:", font=("Roboto", 16, "bold"))
    rotulo.pack(pady=(20, 10), padx=20, anchor="w")

    caixa_texto = ctk.CTkTextbox(janela, height=100, font=("Roboto", 14))
    caixa_texto.pack(pady=(0, 20), padx=20, fill="x")
    caixa_texto.focus() # Já deixa o cursor piscando lá

    botao = ctk.CTkButton(janela, text="Enviar Pacote", command=quando_clicar_enviar, font=("Roboto", 14, "bold"))
    botao.pack(pady=10, padx=20, fill="x")
    
    janela.mainloop()
    return texto_digitado

def show_report(titulo_janela, texto_limpo, texto_cripto, texto_binario, 
                lbl_limpo="1. Mensagem Original:", 
                lbl_cripto="2. Hexadecimal (Criptografado):", 
                lbl_bin="3. Tripa de Bits (Camada Física):"):
    """
    Abre aquele janelão mostrando o passo a passo do que aconteceu.
    """
    janela_relatorio = ctk.CTk()
    janela_relatorio.title(titulo_janela)
    janela_relatorio.geometry("600x600")

    # Scrollable frame (se o texto for muito grande, dá pra rolar)
    area_rolagem = ctk.CTkScrollableFrame(janela_relatorio)
    area_rolagem.pack(fill="both", expand=True, padx=10, pady=10)

    # --- PARTE 1: Texto Normal ---
    lbl1 = ctk.CTkLabel(area_rolagem, text=lbl_limpo, font=("Roboto", 14, "bold"), anchor="w")
    lbl1.pack(fill="x", pady=(10,0))
    
    box1 = ctk.CTkTextbox(area_rolagem, height=60)
    box1.insert("0.0", texto_limpo)
    box1.configure(state="disabled") # Trava pro usuário não zoar o relatório
    box1.pack(fill="x", pady=(5,10))

    # --- PARTE 2: Criptografia ---
    lbl2 = ctk.CTkLabel(area_rolagem, text=lbl_cripto, font=("Roboto", 14, "bold"), anchor="w")
    lbl2.pack(fill="x")
    
    box2 = ctk.CTkTextbox(area_rolagem, height=80)
    box2.insert("0.0", texto_cripto)
    box2.configure(state="disabled")
    box2.pack(fill="x", pady=(5,10))

    # --- PARTE 3: Binário ---
    lbl3 = ctk.CTkLabel(area_rolagem, text=lbl_bin, font=("Roboto", 14, "bold"), anchor="w")
    lbl3.pack(fill="x")
    
    box3 = ctk.CTkTextbox(area_rolagem, height=100)
    box3.insert("0.0", texto_binario)
    box3.configure(state="disabled")
    box3.pack(fill="x", pady=(5,10))

    botao_fechar = ctk.CTkButton(area_rolagem, text="Beleza, pode fechar", command=janela_relatorio.destroy, fg_color="green")
    botao_fechar.pack(pady=20, fill="x")

    janela_relatorio.mainloop()