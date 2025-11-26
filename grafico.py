import matplotlib.pyplot as plt
from matplotlib.widgets import Button

class PlotadorInterativo:
    def __init__(self, lista_sinal, mostrar_quantos=100):
        self.dados = lista_sinal
        self.total = len(lista_sinal)
        self.quanto_mostra = mostrar_quantos
        self.onde_comeca = 0
        
        # Cria a janela do gráfico
        # O 'bottom=0.2' é pra sobrar espaço pros botões lá embaixo
        self.figura, self.eixo = plt.subplots(figsize=(10, 5))
        plt.subplots_adjust(bottom=0.2)
        
        # Truque pro gráfico de degrau ficar certo no final: repete o último ponto
        # Senão o último bit some
        eixo_x = range(self.total + 1)
        eixo_y = self.dados + [self.dados[-1]]
        
        # Desenha a linha azul ('step' faz o formato de onda quadrada)
        self.eixo.step(eixo_x, eixo_y, where='post', linewidth=2, color='#007acc')
        
        # Deixa bonitinho (Eixos Y fixos em -5, 0 e 5)
        self.eixo.set_yticks([-5, 0, 5])
        self.eixo.set_ylim(-6, 6) # Dá uma margem pra não colar na borda
        self.eixo.grid(True, linestyle='--', alpha=0.6) # Gradezinha de fundo
        self.eixo.axhline(0, color='black', linewidth=1) # Linha do zero pra referência
        self.eixo.set_ylabel('Tensão (V)')
        
        # Chama a função que arruma o zoom inicial
        self.atualiza_tela()
        
        # --- BOTÕES ---
        # Posição: [esquerda, baixo, largura, altura]
        posicao_botao1 = plt.axes([0.3, 0.05, 0.15, 0.075])
        posicao_botao2 = plt.axes([0.55, 0.05, 0.15, 0.075])
        
        # Cria os botões e guarda na memória (senão o Python deleta e eles somem/não funcionam)
        self.botao_volta = Button(posicao_botao1, '< Anterior')
        self.botao_vai = Button(posicao_botao2, 'Próximo >')
        
        # Diz o que fazer quando clica
        self.botao_volta.on_clicked(self.voltar)
        self.botao_vai.on_clicked(self.avancar)
        
        plt.show()

    def atualiza_tela(self):
        """ Só muda o zoom do eixo X pra parecer que tá paginando """
        inicio = self.onde_comeca
        fim = inicio + self.quanto_mostra
        
        # Define o limite do Zoom
        self.eixo.set_xlim(inicio, fim)
        
        # Título dinâmico pra saber onde tá
        self.eixo.set_title(f'Visualizando Sinal MLT-3 (Amostras {inicio} até {min(fim, self.total)})')
        
        # Manda redesenhar
        plt.draw()

    def avancar(self, evento):
        # Só avança se não tiver chegado no fim da lista
        if self.onde_comeca + self.quanto_mostra < self.total:
            self.onde_comeca += self.quanto_mostra
            self.atualiza_tela()

    def voltar(self, evento):
        # Só volta se não tiver no começo
        if self.onde_comeca - self.quanto_mostra >= 0:
            self.onde_comeca -= self.quanto_mostra
            self.atualiza_tela()