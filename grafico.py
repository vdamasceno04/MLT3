import matplotlib.pyplot as plt
from matplotlib.widgets import Button

class PlotadorInterativo:
    def __init__(self, signal_data, bits_por_pagina=100):
        self.signal = signal_data
        self.total_bits = len(signal_data)
        self.page_size = bits_por_pagina
        self.current_start = 0
        
        # Configura a Figura e o Eixo
        # Espaço embaixo (bottom=0.2) para os botões
        self.fig, self.ax = plt.subplots(figsize=(10, 5))
        plt.subplots_adjust(bottom=0.2)
        
        # Plota o sinal INTEIRO uma vez
        # Adicionamos o último ponto repetido para fechar o degrau visualmente
        x_axis = range(self.total_bits + 1)
        y_axis = self.signal + [self.signal[-1]]
        self.ax.step(x_axis, y_axis, where='post', linewidth=2, color='#007acc')
        
        # Configurações visuais fixas
        self.ax.set_yticks([-5, 0, 5])
        self.ax.set_ylim(-6, 6)
        self.ax.grid(True, which='both', linestyle='--', alpha=0.6)
        self.ax.axhline(0, color='black', linewidth=1)
        self.ax.set_ylabel('Tensão (Volts)')
        
        # Inicializa a primeira visualização
        self.atualizar_visualizacao()
        
        # --- CRIAÇÃO DOS BOTÕES ---
        # Define a posição dos botões [x, y, largura, altura]
        ax_prev = plt.axes([0.3, 0.05, 0.15, 0.075])
        ax_next = plt.axes([0.55, 0.05, 0.15, 0.075])
        
        # Cria os objetos Button e guarda referências 
        self.btn_prev = Button(ax_prev, '< Anterior')
        self.btn_next = Button(ax_next, 'Próximo >')
        
        # Conecta os cliques às funções
        self.btn_prev.on_clicked(self.voltar_pagina)
        self.btn_next.on_clicked(self.avancar_pagina)
        
        plt.show()

    def atualizar_visualizacao(self):
        """Atualiza o limite do eixo X para criar o efeito de paginação"""
        start = self.current_start
        end = start + self.page_size
        
        # Define o limite do Zoom no eixo X
        self.ax.set_xlim(start, end)
        
        # Atualiza o Título com a posição atual
        self.ax.set_title(f'Codificação MLT-3 (Bits {start} a {min(end, self.total_bits)} de {self.total_bits})')
        
        # Força o redesenho do gráfico
        plt.draw()

    def avancar_pagina(self, event):
        if self.current_start + self.page_size < self.total_bits:
            self.current_start += self.page_size
            self.atualizar_visualizacao()

    def voltar_pagina(self, event):
        if self.current_start - self.page_size >= 0:
            self.current_start -= self.page_size
            self.atualizar_visualizacao()

