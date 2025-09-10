import tkinter as tk
from tkinter import scrolledtext

def getSentence() -> str:
    result_string = ""
    root = tk.Tk()
    root.title("Digite a Frase")
    root.geometry("450x300")
    root.attributes("-topmost", True)

    def on_confirm():
        nonlocal result_string
        content = text_area.get("1.0", tk.END)
        result_string = content
        root.destroy()

    label = tk.Label(root, text="Digite seu texto e clique em Confirmar:", padx=10, pady=10)
    label.pack()

    text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Helvetica", 11), height=10, width=50)
    text_area.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)
    text_area.focus()

    confirm_button = tk.Button(root, text="Confirmar", command=on_confirm)
    confirm_button.pack(pady=10)
    
    root.mainloop()

    return result_string