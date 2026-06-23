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
        caixa_hor = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL, 
            homogeneous=False, 
            spacing=10
        )
        

        self.nome = Gtk.Entry()
        self.nome.set_placeholder_text("Nome")
        caixa_hor.add(self.nome)

        self.combo = Gtk.ComboBoxText()
        self.combo.append("info", "Informática")
        self.combo.append("meca", "Mecatrônica")
        self.combo.append("edif", "Edificações")
        self.combo.set_active_id("info")
        caixa_hor.add(self.combo)

        caixa_ver = Gtk.Box(
            orientation=Gtk.Orientation.HORIZONTAL,
            homogeneous=False,
            spacing=10
        )
        caixa_hor.add(caixa_ver)

        self.text = Gtk.Label(label="Quer certificado?")
        caixa_ver.pack_start(self.text, False, False, 10)

        self.check = Gtk.CheckButton(label="Sim")
        caixa_hor.add(self.check)

        btn_salvar = Gtk.Button(label="Salvar")
        btn_salvar.connect("clicked", self.salvar_dados)
        caixa_hor.add(btn_salvar)

        janela.add(caixa_hor)
        janela.show_all()

    def sair(self, componente=None, dados=None):
        Gtk.main_quit()


    def salvar_dados(self, componente=None, dados=None):
        nome_txt = self.nome.get_text()
        combo_txt = self.combo.get_active_text()
        check_text = self.check.get_active()
        if check_text:
            print(f"Nome: {nome_txt} - Curso: {combo_txt} - Quer Certificado: Sim")
        else:
            print(f"Nome: {nome_txt} - Curso: {combo_txt} - Quer Certificado: Não")
        


if __name__ == "__main__":
    tela1 = Tela()
    Gtk.main()
