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

        # Box
        caixa = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL, 
            homogeneous=False, 
            spacing=10
        )

        btn_amor = Gtk.Button()
        btn_amor.set_label("Amor")
        btn_amor.connect("clicked", self.imprimir, 2)
        caixa.add(btn_amor)

        btn_presente = Gtk.Button()
        btn_presente.set_label("Presente")
        btn_presente.connect("clicked", self.imprimir, 3)
        caixa.add(btn_presente)

        btn_coracao = Gtk.Button()
        btn_coracao.set_label("Coração <3")
        btn_coracao.connect("clicked", self.imprimir, 4)
        caixa.add(btn_coracao)

        janela.add(caixa)
        janela.show_all()

    def sair(self, componente=None, dados=None):
        Gtk.main_quit()

    def imprimir(self, componente=None, dados=None):
        msg = componente.get_label()
        print(f":) {msg*dados}")

if __name__ == "__main__":
    tela1 = Tela()
    Gtk.main()
