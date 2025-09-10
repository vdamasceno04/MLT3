import interface

print("Vamos chamar a interface para pegar uma frase.")

frase = interface.getSentence()

# O programa principal continua a execução após a janela da interface ser fechada.
if frase:
    print("\nO programa principal recebeu as seguintes frases:")
    
    print({frase})
    
    print("\nProcessamento finalizado.")
else:
    print("\nNenhuma frase foi recebida. O programa principal vai encerrar.")