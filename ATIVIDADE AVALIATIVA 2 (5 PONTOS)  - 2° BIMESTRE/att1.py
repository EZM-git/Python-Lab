import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Aplicacao:
   def __init__(self):
       janela = Gtk.Window()
       janela.set_title("GUI com Python e Gtk") 				  
       janela.set_default_size(400, 200)		
       rotulo = Gtk.Label()
       rotulo.set_label("NATHAN MAZZARO PEREIRA\n 2º Informática")
       janela.add(rotulo)
       janela.connect("destroy", Gtk.main_quit)
       rotulo.show()
       janela.show()

if __name__ == '__main__':
   prog = Aplicacao()
   Gtk.main()
