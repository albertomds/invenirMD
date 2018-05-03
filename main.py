#!/usr/bin/env python2.7

# main.py

import wx

#Define Tamanho da Janela
class Tamanho(wx.Frame):

    def __init__(self, parent, title):
        super(Tamanho, self).__init__(parent, title=title, size=(550, 600))
        self.Centre()

#Janela Principal
def main():
    principal = wx.App()

    frame1 = Tamanho(None, title='Invenir_v0.1a')
    frame1.Show()

    principal.MainLoop()

if __name__ == '__main__':
        main()
