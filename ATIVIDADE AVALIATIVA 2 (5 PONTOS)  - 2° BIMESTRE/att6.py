#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk 

class Tela:
    def __init__(self):
        self.janela = Gtk.Window()
        self.janela.connect("delete-event", self.sair)
        self.janela.set_title("Título da self.janela")
        self.janela.set_border_width(20)
        self.janela.set_default_size(400, 300)

        # Box
        self.caixa = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL, 
            homogeneous=False, 
            spacing=10
        )
        
        self.nota1 = Gtk.Entry()
        self.nota1.set_placeholder_text("Nota 1")
        self.caixa.add(self.nota1)

        self.nota2 = Gtk.Entry()
        self.nota2.set_placeholder_text("Nota 2")
        self.caixa.add(self.nota2)

        self.nota3 = Gtk.Entry()
        self.nota3.set_placeholder_text("Nota 3")
        self.caixa.add(self.nota3)

        btn = Gtk.Button(label="Calcular Média")
        btn.connect("clicked", self.calcular_media)
        self.caixa.add(btn)

        self.lbl_msg = Gtk.Label(label="")
        self.caixa.add(self.lbl_msg)

        self.janela.add(self.caixa)
        self.janela.show_all()

    def sair(self, componente=None, dados=None):
        Gtk.main_quit()

    def calcular_media(self, componente=None, dados=None):
        try:
            valor1 = float(self.nota1.get_text())
            valor2 = float(self.nota2.get_text())
            valor3 = float(self.nota3.get_text())
            media = (valor1+valor2+valor3)/3

            notas_validas = all(0 <= v <= 10 for v in (valor1, valor2, valor3)) # Cabei de aprender na internet, serve para diminuir a utilização de muitas checagens de valores

            if notas_validas:

                if media >= 6:
                    self.lbl_msg.set_markup("<span foreground='green'><b>Aprovado</b></span>")

                else:
                    self.lbl_msg.set_markup("<span foreground='red'><b>Recuperação</b></span>")

                    self.nota_rec = Gtk.Entry()
                    self.nota_rec.set_placeholder_text("Nota da Recuperação")
                    self.caixa.add(self.nota_rec)

                    btn_rec = Gtk.Button(label="Calcular Recuperação")
                    btn_rec.connect("clicked", self.calcular_recuperacao)
                    self.caixa.add(btn_rec)

                    self.lbl_msg2 = Gtk.Label(label="")
                    self.caixa.add(self.lbl_msg2)

                    self.janela.show_all()

            else:
                self.lbl_msg.set_label("Valores Válidos (0-10)")

        except ValueError:
            self.lbl_msg.set_label("Entrada Inválida")

    def calcular_recuperacao(self, componente=None, dados=None):
        try:
            valor1 = float(self.nota1.get_text())
            valor2 = float(self.nota2.get_text())
            valor3 = float(self.nota3.get_text())
            valor_rec = float(self.nota_rec.get_text())

            media = (valor1+valor2+valor3+valor_rec)/4

            notas_validas = all(0 <= v <= 10 for v in (valor1, valor2, valor3, valor_rec))

            if notas_validas:

                if media >= 6:
                    self.lbl_msg2.set_markup("<span foreground='green'><b>Aprovado</b></span>")

                else:
                    self.lbl_msg2.set_markup("<span foreground='red'><b>Reprovado</b></span>")

            else:
                self.lbl_msg2.set_label("Valores Válidos (0-10)")

        except ValueError:
            self.lbl_msg2.set_label("Entrada Inválida")

if __name__ == "__main__":
    tela1 = Tela()
    Gtk.main()
