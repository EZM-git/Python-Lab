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
        
        self.texto_peso = Gtk.Entry()
        self.texto_peso.set_placeholder_text("Peso(Kg)")
        caixa.add(self.texto_peso)

        self.texto_altura = Gtk.Entry()
        self.texto_altura.set_placeholder_text("Altura(m)")
        caixa.add(self.texto_altura)

        btn = Gtk.Button(label="Calcular IMC")
        btn.connect("clicked", self.calcular_imc)
        caixa.add(btn)

        self.lbl_msg = Gtk.Label(label="")
        caixa.add(self.lbl_msg)

        janela.add(caixa)
        janela.show_all()

    def sair(self, componente=None, dados=None):
        Gtk.main_quit()

    def calcular_imc(self, componente=None, dados=None):
        try:
            peso = float(self.texto_peso.get_text())
            altura = float(self.texto_altura.get_text())
            imc = peso / (altura ** 2)

            if imc < 18.5:
                self.lbl_msg.set_label("Abaixo do Peso")

            if 18.5 <= imc < 24.9:
                self.lbl_msg.set_label("Normal")

            if 25.0 <= imc < 29.9:
                self.lbl_msg.set_label("Sobrepeso")

            if 30.0 <= imc < 34.9:
                self.lbl_msg.set_label("Obesidade I")

            if 35 <= imc < 40:
                self.lbl_msg.set_label("Obesidade II")

            if imc >= 40.0:
                self.lbl_msg.set_label("Obesidade III")

        except ValueError:
            self.lbl_msg.set_label("Entrada inválida")

if __name__ == "__main__":
    tela1 = Tela()
    Gtk.main()