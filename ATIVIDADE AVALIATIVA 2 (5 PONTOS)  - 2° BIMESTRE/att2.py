import gi
gi.require_version("Gtk", "3.0") # Ou "4.0" se preferir a versão mais recente
from gi.repository import Gtk

class ContadorCliques(Gtk.Window):
    def __init__(self):
        super().__init__(title="Contador de Cliques")
        self.set_border_width(20)
        self.set_default_size(200, 150)

        # Variável para armazenar a contagem
        self.quantidade = 0

        # Cria uma caixa vertical (Gtk.Box) para organizar os elementos
        caixa = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(caixa)

        # Cria o rótulo inicial com o número "0"
        self.rotulo = Gtk.Label()
        self.rotulo.set_text(str(self.quantidade))
        caixa.pack_start(self.rotulo, True, True, 0)

        # Cria o botão com o texto "Clique Aqui!"
        botao = Gtk.Button(label="Clique Aqui!")
        
        # Conecta o sinal de clique do botão à função de callback
        botao.connect("clicked", self.ao_clicar_botao)
        caixa.pack_start(botao, True, True, 0)

    # Função chamada quando o botão é clicado
    def ao_clicar_botao(self, widget):
        self.quantidade += 1 # Incrementa a variável
        self.rotulo.set_text(str(self.quantidade)) # Atualiza o rótulo

# Inicializa a aplicação
win = ContadorCliques()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
