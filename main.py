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

        # Prepara visualização Hex da criptografia (mais bonito que bytes brutos)
        cripto_hex = bytes_criptografados.hex().upper()

        interface.show_report("Host A - Processamento", frase_completa, cripto_hex, stream_binaria)
        
        # Gráfico
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
    
    # Gráfico (Mostra o sinal físico que chegou)
    grafico.PlotadorInterativo(sinal_recebido)
    
    # Decodificação
    stream_binaria_recuperada = mlt3.mlt3_decode(sinal_recebido)
    bytes_criptografados_recuperados = encryption.binary_stream_to_bytes(stream_binaria_recuperada)
    
    try:
        bytes_originais_recuperados = encryption.decrypt(bytes_criptografados_recuperados)
        frase_final = bytes_originais_recuperados.decode('latin-1') 
        
        cripto_hex = bytes_criptografados_recuperados.hex().upper()
        
        interface.show_report(
            titulo="Host B - Relatório de Decodificação", 
            texto_claro=frase_final, 
            texto_cripto=cripto_hex, 
            texto_binario=stream_binaria_recuperada,
            lbl_claro="3. MENSAGEM FINAL RECUPERADA:",
            lbl_cripto="2. Dados Criptografados Recebidos:",
            lbl_bin="1. Stream Binária Demodulada:"
        )
        
    except Exception as e:
        print(f"Erro na descriptografia: {e}")