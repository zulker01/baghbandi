# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 11:04:02 2022

@author: User
"""

from tkinter import *


    
class baghClass():
    #baghphoto  = PhotoImage(file="bagh.png")
    def __init__(self,x,y,canvas,baghPhoto):
        self.x=x
        self.y = y
        self.canvas = canvas
        self.baghPhoto=baghPhoto
        
        self.draw_bagh()
        
        
    def draw_bagh(self):
        self.baghImg = self.canvas.create_image(self.x, self.y,  image=self.baghPhoto) # bagh image created
      

class goatClass():
    #baghphoto  = PhotoImage(file="bagh.png")
    def __init__(self,x,y,canvas,goatPhoto):
        self.x=x
        self.y = y
        self.canvas = canvas
        self.goatPhoto=goatPhoto
        
        self.draw_goat()
        
        
    def draw_goat(self):
        self.goat = self.canvas.create_image(self.x, self.y,  image=self.goatPhoto) # bagh image created
      
