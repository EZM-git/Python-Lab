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
        
        self.texto_usu = Gtk.Entry()
        self.texto_usu.set_placeholder_text("Usuário")
        caixa.add(self.texto_usu)

        self.texto_senha = Gtk.Entry()
        self.texto_senha.set_placeholder_text("Senha")
        self.texto_senha.set_visibility(False) 
        caixa.add(self.texto_senha)

        btn = Gtk.Button(label="Entrar")
        btn.connect("clicked", self.checar_dados)
        caixa.add(btn)

        # Atributo da classe, acessível em outros métodos
        self.lbl_msg = Gtk.Label(label="")
        caixa.add(self.lbl_msg)

        janela.add(caixa)
        janela.show_all()

    def sair(self, componente=None, dados=None):
        Gtk.main_quit()

    def checar_dados(self, componente=None, dados=None):
        usuario = self.texto_usu.get_text()
        senha = self.texto_senha.get_text()
        if usuario == "admin" and senha == "123":
            self.lbl_msg.set_markup("<span foreground='green'><b>Acesso Liberado</b></span>")
        else:
            self.lbl_msg.set_markup("<span foreground='red'><b>Acesso Liberado</b></span>")


if __name__ == "__main__":
    tela1 = Tela()
    Gtk.main()
