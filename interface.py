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

    # Layout usando Grid 
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=1)

    label = ctk.CTkLabel(root, text="Mensagem para Codificação", font=("Roboto", 16, "bold"))
    label.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="w")

    # Caixa de texto 
    text_area = ctk.CTkTextbox(root, font=("Roboto", 14), corner_radius=10)
    text_area.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="nsew")
    text_area.focus()

    confirm_button = ctk.CTkButton(
        root, 
        text="Criptografar e Enviar", 
        command=on_confirm,
        height=40,
        font=("Roboto", 14, "bold")
    )
    confirm_button.grid(row=2, column=0, padx=20, pady=(0, 20), sticky="ew")
    
    root.mainloop()

    return result_string

