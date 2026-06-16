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
        
        self.real = Gtk.Entry()
        self.real.set_placeholder_text("Reais (R$)")
        caixa.add(self.real)

        btn_dolar = Gtk.Button(label="Converter para Dólar")
        btn_dolar.connect("clicked", self.converter_dolar)
        caixa.add(btn_dolar)

        btn_euro = Gtk.Button(label="Converter para Euro")
        btn_euro.connect("clicked", self.converter_euro)
        caixa.add(btn_euro)

        btn_bitcoin = Gtk.Button(label="Converter para Bitcoin")
        btn_bitcoin.connect("clicked", self.converter_bitcoin)
        caixa.add(btn_bitcoin)

        self.lbl_msg = Gtk.Label(label="")
        caixa.add(self.lbl_msg)

        janela.add(caixa)
        janela.show_all()

    def sair(self, componente=None, dados=None):
        Gtk.main_quit()

    def converter_dolar(self, componente=None, dados=None):
        # Preço na hora de escrever o código: 1USD = R$5.08
        real = float(self.real.get_text())
        dolar = real / 5.08
        self.lbl_msg.set_label(f"R${real} = ${dolar:.2f}")

    def converter_euro(self, componente=None, dados=None):
        # Preço na hora de escrever o código: 1Euro = R$5.88
        real = float(self.real.get_text())
        euro = real / 5.88
        self.lbl_msg.set_label(f"R${real} = €{euro:.2f}")

    def converter_bitcoin(self, componente=None, dados=None):
        # Preço na hora de escrever o código: 1BTC = R$336.677,51
        real = float(self.real.get_text())
        btc = real / 336677.51
        self.lbl_msg.set_label(f"R${real} =  ₿{btc:.2f}")

if __name__ == "__main__":
    tela1 = Tela()
    Gtk.main()