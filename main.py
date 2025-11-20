import interface
import encryption
import mlt3
import grafico
import rede 

print("--- TRABALHO DE COMUNICAÇÃO DE DADOS ---")
modo = input("Escolha o modo:\n[1] HOST A (Enviar)\n[2] HOST B (Receber)\n> ")

if modo == '1':
    # =================================================================
    # FLUXO DO HOST A (TRANSMISSOR)
    # =================================================================
    
    # 1. Interface e Input
    frase_lista = interface.getSentence() # Sua função original
    frase_completa = frase_lista.strip() # Caso sua função retorne lista

    if frase_completa.strip():
        # 2. Criptografia e Binário
        bytes_originais = encryption.to_bytes(frase_completa)
        bytes_criptografados = encryption.encrypt(bytes_originais)
        stream_binaria = encryption.to_binary_stream(bytes_criptografados)
        
        # 3. Codificação de Linha
        sinal_mlt3 = mlt3.mlt3_encode(stream_binaria)

        print("\n--- HOST A: DADOS PROCESSADOS ---")
        print(f"Frase Original: {frase_completa}")
        print(f"Binário Cripto: {stream_binaria[:50]}...") # Mostra só o começo pra não poluir
        
        # 4. Plotar Gráfico de Envio (Bloqueia até fechar a janela)
        print("Feche o gráfico para continuar o envio...")
        grafico.PlotadorInterativo(sinal_mlt3)

        # 5. Enviar pela Rede
        ip_destino = input("\nDigite o IP do Host B: ")
        rede.enviar_sinal(ip_destino, sinal_mlt3)
        
    else:
        print("Nenhuma frase digitada.")

elif modo == '2':
    # =================================================================
    # FLUXO DO HOST B (RECEPTOR)
    # =================================================================
    
    # 1. Esperar receber o sinal pela rede
    print("\n--- HOST B: MODO ESCUTA ---")
    sinal_recebido = rede.receber_sinal()
    
    print(f"\nSinal Recebido ({len(sinal_recebido)} amostras).")
    
    # 2. Plotar Gráfico de Recepção (Requisito T2 e T8)
    print("Feche o gráfico para continuar a decodificação...")
    grafico.PlotadorInterativo(sinal_recebido)
    
    # 3. Processo Inverso: Decodificar MLT-3 -> Binário
    stream_binaria_recuperada = mlt3.mlt3_decode(sinal_recebido)
    
    # 4. Processo Inverso: Binário -> Bytes
    bytes_criptografados_recuperados = encryption.binary_stream_to_bytes(stream_binaria_recuperada)
    
    # 5. Processo Inverso: Descriptografar
    try:
        bytes_originais_recuperados = encryption.decrypt(bytes_criptografados_recuperados)
        frase_final = bytes_originais_recuperados.decode('latin-1') 
        
        print("\n--- MENSAGEM RECUPERADA ---")
        print(f"Conteúdo: {frase_final}")
        
        # Mostra na interface
        import tkinter as tk
        from tkinter import messagebox
        root = tk.Tk()
        root.withdraw()
        messagebox.showinfo("Mensagem Recebida", f"A mensagem foi:\n\n{frase_final}")
        root.destroy()
        
    except Exception as e:
        print(f"Erro na descriptografia: {e}")
        print("Verifique se a chave é a mesma em ambas as máquinas!")

else:
    print("Opção inválida.")