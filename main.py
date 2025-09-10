import interface
import encryption
import mlt3

print("Vamos chamar a interface para pegar uma frase.")

frase_lista = interface.getSentence()

frase_completa = "\n".join(frase_lista)

if frase_completa.strip():

    bytes_originais = encryption.to_bytes(frase_completa)
    bytes_criptografados = encryption.encrypt(bytes_originais)

    stream_binaria = encryption.to_binary_stream(bytes_criptografados)
    
    sinal_mlt3 = mlt3.mlt3_encode(stream_binaria)

    print("\nO programa principal recebeu as seguintes frases:")
    
    print(f"Frases Recebidas: {frase_lista}")
    print(f"Binário      : {encryption.to_binary_stream(bytes_originais)}")
    print(f"Criptografado: {encryption.to_binary_stream(bytes_criptografados)}")
    
    print("\nProcessamento finalizado.")
else:
    print("\nNenhuma frase foi recebida. O programa principal vai encerrar.")