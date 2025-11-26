import grafico
import mlt3

# --- BLOCO DE TESTE ---
if __name__ == "__main__":
    input_binaria = "01011100101"

    sinal_mlt3 = mlt3.mlt3_encode(input_binaria)

    grafico.PlotadorInterativo(sinal_mlt3)

    output_binaria = mlt3.mlt3_decode(sinal_mlt3)

    print("-" * 30)
    print(f"Entrada Original:  {input_binaria}")
    print(f"Sinal MLT-3:       {sinal_mlt3}")
    print(f"Saída Decodificada:{output_binaria}")
    print("-" * 30)

    if input_binaria == output_binaria:
        print("SUCESSO: O binário decodificada é igual ao original.")
    else:
        print("ERRO: os binários são diferentes.")