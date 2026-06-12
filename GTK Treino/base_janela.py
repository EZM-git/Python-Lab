#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk 

class Tela:
    def __init__(self):
        janela = Gtk.Window()
        janela.connect("delete-event", self.sair)
        janela.set_title("Título da janela")
        janela.set_border_width(20)
        janela.set_default_size(400, 300)

        janela.show_all()

    def sair(self, componente=None, dados=None):
        Gtk.main_quit()

if __name__ == "__main__":
    tela1 = Tela()
    Gtk.main()
    
