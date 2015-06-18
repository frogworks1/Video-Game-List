#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode Tkinter tutorial

This script shows a simple window
on the screen.

author: Jan Bodnar
last modified: January 2011
website: www.zetcode.com
"""

from Tkinter import Tk, Frame, BOTH


class VGmain(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent, background="#6A8FAE")   
         
        self.parent = parent
        self.parent.title("Centered window")
        self.pack(fill=BOTH, expand=1)
        self.centerWindow()
    
    def centerWindow(self):

        w = 750
        h = 650

        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()

        x = (sw - w)/2
        y = (sh - h)/2
        
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))
      
        self.parent.title("Video Game List")
        

def main():
  
    root = Tk()
    ex = VGmain(root)
    root.mainloop()  


if __name__ == '__main__':
    main()
