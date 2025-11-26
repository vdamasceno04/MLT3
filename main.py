import interface
import encryption
import mlt3
import grafico
import rede 

print("--- TRABALHO DE COMUNICAÇÃO DE DADOS ---")
print("Quem é você na fila do pão?")
modo = input("[1] HOST A (Manda)\n[2] HOST B (Recebe)\n> ")

if modo == '1':
    # =================================================================
    # LADO A: O CARA QUE MANDA
    # =================================================================
    
    # Pega o texto da interface gráfica ou console
    texto_baguncado = interface.getSentence() 
    texto_limpo = texto_baguncado.strip()

    if texto_limpo:
        # Transforma texto em bytes e tranca com a senha
        bytes_normais = encryption.texto_pra_bytes(texto_limpo)
        bytes_trancados = encryption.criptografar_tudo(bytes_normais)
        
        # Vira aquela tripa de 0 e 1 (string gigante)
        tripa_bits = encryption.bytes_pra_binario_string(bytes_trancados)
        
        # Aplica o MLT-3 pra virar sinal "elétrico" (V, 0, -V)
        sinal_pronto = mlt3.mlt3_encode(tripa_bits)

        # Só pra ficar bonito no print (hexadecimal)
        visual_hex = bytes_trancados.hex().upper()

        interface.show_report("Host A - Enviando...", texto_limpo, visual_hex, tripa_bits)
        
        # Mostra o gráfico do sinal saindo
        grafico.PlotadorInterativo(sinal_pronto)

        # Manda ver na rede
        ip_do_amigo = input("\nQual o IP do camarada (Host B)? ")
        rede.enviar_sinal(ip_do_amigo, sinal_pronto)
        
    else:
        print("Escreve alguma coisa né...")

elif modo == '2':
    # =================================================================
    # LADO B: O CARA QUE RECEBE
    # =================================================================
    
    print("\n--- HOST B: FICA ESPERANDO ---")
    # Fica travado aqui até chegar algo
    sinal_que_chegou = rede.receber_sinal()
    
    print(f"\nChegou coisa! ({len(sinal_que_chegou)} amostras).")
    
    # Mostra o que chegou 
    grafico.PlotadorInterativo(sinal_que_chegou)
    
    # Tenta desfazer a bagunça
    # 1. Tira do MLT-3 e volta pra 0 e 1
    bits_recuperados = mlt3.mlt3_decode(sinal_que_chegou)
    
    # 2. Junta os bits em bytes de novo (ainda criptografados)
    bytes_trancados_volta = encryption.binario_string_pra_bytes(bits_recuperados)
    
    try:
        # 3. Tenta destrancar com a senha
        bytes_destrancados = encryption.descriptografar_tudo(bytes_trancados_volta)
        mensagem_final = encryption.bytes_pra_texto(bytes_destrancados) 
        
        visual_hex = bytes_trancados_volta.hex().upper()
        
        interface.show_report(
            titulo="Host B - Sucesso", 
            texto_claro=mensagem_final, 
            texto_cripto=visual_hex, 
            texto_binario=bits_recuperados,
            lbl_claro="3. MENSAGEM FINAL:",
            lbl_cripto="2. O que chegou trancado:",
            lbl_bin="1. Bits brutos:"
        )
        
    except Exception as e:
        print(f"Deu ruim pra descriptografar: {e}")