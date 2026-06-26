#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk 

class Tela:
    def __init__(self):
        janela = Gtk.Window()
        janela.connect("delete-event", self.sair)
        janela.set_title("Calculadora")
        janela.set_border_width(20)
        janela.set_default_size(265, 250)
        janela.set_resizable(False)

        # Boxes
        frame = Gtk.Frame()
        frame.set_size_request(50, 50)
        caixa = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL, 
            homogeneous=False, 
            spacing=10
        )
        caixa_hor_0 = Gtk.Box(
            orientation=Gtk.Orientation.HORIZONTAL, 
            homogeneous=False, 
            spacing=10
        )
        caixa_hor_1 = Gtk.Box(
            orientation=Gtk.Orientation.HORIZONTAL, 
            homogeneous=False, 
            spacing=10
        )
        caixa_hor_2 = Gtk.Box(
            orientation=Gtk.Orientation.HORIZONTAL,
            homogeneous=False,
            spacing=10
        )
        caixa_hor_3 = Gtk.Box(
            orientation=Gtk.Orientation.HORIZONTAL,
            homogeneous=False,
            spacing=10
        )
        caixa_hor_4 = Gtk.Box(
            orientation=Gtk.Orientation.HORIZONTAL, 
            homogeneous=False,
            spacing=10
        )
        caixa_hor_5 = Gtk.Box(
            orientation=Gtk.Orientation.HORIZONTAL, 
            homogeneous=False,
            spacing=10
        )
        
        # Caixa de Texto
        self.valor_visor = "0"
        self.telinha = Gtk.Label(label="<big></big>", use_markup=True)
        self.telinha.set_justify(Gtk.Justification.RIGHT)
        caixa_hor_0.pack_end(self.telinha, expand=False, fill=False, padding=20)

        # Botões
        btn_1 = ["ON", "C"]
        for texto in btn_1:
            btn = Gtk.Button(label=texto)
            btn.connect("clicked", self.calculo)
            caixa_hor_1.add(btn)
        
        btn_raiz = Gtk.Button(label="√")
        btn_raiz.connect("clicked", self.calculo)
        caixa_hor_1.pack_end(btn_raiz, expand=False, fill=False, padding=11)

        btn_2 = ["7", "8", "9", "+"]
        for texto in btn_2:
            btn = Gtk.Button(label=texto)
            btn.connect("clicked", self.calculo)
            caixa_hor_2.add(btn)

        btn_3 = ["4", "5", "6", "-"]
        for texto in btn_3:
            btn = Gtk.Button(label=texto)
            btn.connect("clicked", self.calculo)
            caixa_hor_3.add(btn)

        btn_4 = ["1", "2", "3", "*"]
        for texto in btn_4:
            btn = Gtk.Button(label=texto)
            btn.connect("clicked", self.calculo)
            caixa_hor_4.add(btn)
        
        btn_0 = Gtk.Button(label="0")
        btn_0.connect("clicked", self.calculo)
        caixa_hor_5.pack_start(btn_0, expand=False, fill=False, padding=0)

        btn_igual = Gtk.Button(label="=")
        btn_igual.connect("clicked", self.calculo)
        caixa_hor_5.pack_start(btn_igual, expand=True, fill=True, padding=0)

        btn_divisao =  Gtk.Button(label="/")
        btn_divisao.connect("clicked", self.calculo)
        caixa_hor_5.pack_end(btn_divisao, expand=False, fill=True, padding=11)

        frame.add(caixa_hor_0)
        caixa.add(frame)
        caixa.add(caixa_hor_1)
        caixa.add(caixa_hor_2)
        caixa.add(caixa_hor_3)
        caixa.add(caixa_hor_4)
        caixa.add(caixa_hor_5)
        janela.add(caixa)
        janela.show_all()

    def sair(self, componente=None, dados=None):
        Gtk.main_quit()

    def calculo(self, componente=None, dados=None):
        informacao = componente.get_label()
        if informacao in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            if self.valor_visor == "0":
                self.valor_visor = ""
                self.valor_visor += informacao
                self.telinha.set_label(self.valor_visor)
            else:
                self.valor_visor += informacao
                self.telinha.set_label(self.valor_visor)


if __name__ == "__main__":
    tela1 = Tela()
    Gtk.main()
