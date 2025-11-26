import customtkinter as ctk

def getSentence() -> str:
    result_string = ""
    
    # Configuração do tema Dark Blue 
    ctk.set_appearance_mode("Dark")  
    ctk.set_default_color_theme("blue") 

    root = ctk.CTk() 
    root.title("Host A - Input")
    
    # Centralizar
    w, h = 500, 350
    ws, hs = root.winfo_screenwidth(), root.winfo_screenheight()
    x, y = (ws/2) - (w/2), (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root.attributes("-topmost", True)

    def on_confirm():
        nonlocal result_string
        result_string = text_area.get("1.0", "end-1c")
        root.destroy()

    label = ctk.CTkLabel(root, text="Digite a Mensagem:", font=("Roboto", 16, "bold"))
    label.pack(pady=(20, 10), padx=20, anchor="w")

    text_area = ctk.CTkTextbox(root, height=100, font=("Roboto", 14))
    text_area.pack(pady=(0, 20), padx=20, fill="x")
    text_area.focus()

    btn = ctk.CTkButton(root, text="Processar e Enviar", command=on_confirm, font=("Roboto", 14, "bold"))
    btn.pack(pady=10, padx=20, fill="x")
    
    root.mainloop()
    return result_string

def show_report(titulo, texto_claro, texto_cripto, texto_binario, 
                lbl_claro="1. Mensagem Original:", 
                lbl_cripto="2. Dados Criptografados (Hex):", 
                lbl_bin="3. Stream Binária (Bits):"):
    """
    Exibe uma janela com os dados processados.
    Permite personalizar os rótulos para diferenciar Envio de Recepção.
    """
    root = ctk.CTk()
    root.title(titulo)
    root.geometry("600x600")

    # Scrollable frame
    scroll = ctk.CTkScrollableFrame(root)
    scroll.pack(fill="both", expand=True, padx=10, pady=10)

    # 1. Texto Claro (Pode ser o original ou o recuperado)
    lbl1 = ctk.CTkLabel(scroll, text=lbl_claro, font=("Roboto", 14, "bold"), anchor="w")
    lbl1.pack(fill="x", pady=(10,0))
    box1 = ctk.CTkTextbox(scroll, height=60)
    box1.insert("0.0", texto_claro)
    box1.configure(state="disabled")
    box1.pack(fill="x", pady=(5,10))

    # 2. Criptografia
    lbl2 = ctk.CTkLabel(scroll, text=lbl_cripto, font=("Roboto", 14, "bold"), anchor="w")
    lbl2.pack(fill="x")
    box2 = ctk.CTkTextbox(scroll, height=80)
    box2.insert("0.0", texto_cripto)
    box2.configure(state="disabled")
    box2.pack(fill="x", pady=(5,10))

    # 3. Binário
    lbl3 = ctk.CTkLabel(scroll, text=lbl_bin, font=("Roboto", 14, "bold"), anchor="w")
    lbl3.pack(fill="x")
    box3 = ctk.CTkTextbox(scroll, height=100)
    box3.insert("0.0", texto_binario)
    box3.configure(state="disabled")
    box3.pack(fill="x", pady=(5,10))

    btn = ctk.CTkButton(scroll, text="Fechar / Continuar", command=root.destroy, fg_color="green")
    btn.pack(pady=20, fill="x")

    root.mainloop()