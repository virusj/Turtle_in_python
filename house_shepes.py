# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 20:40:00 2021

@author: JABIR
"""


import turtle as t

#grass
def grass(x,y):
    
    t.color("forestgreen")
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    for i in range(4):
        t.fd(1300)
        t.right(90)
        t.fd(500)
    t.end_fill()
    
#road
def road(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color("black")
    t.begin_fill()
    for i in range(2):
        t.fd(1300)
        t.right(90)
        t.fd(120)
        t.right(90)
    t.end_fill()
    
def dot(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color("white")
    t.begin_fill()
    for i in range(2):
        t.fd(70)
        t.left(90)
        t.fd(20)
        t.left(90)
    t.end_fill()

#SUN
def Sun(x,y,size):
    t.color("yellow")
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    t.circle(size)
    t.end_fill()
  
    
#cloud
def cloud(x,y,z):
    t.penup()
    t.goto(x,y)
    t.color('white')
    t.pendown()
    t.begin_fill()
    t.circle(30)
    t.end_fill()
    
    
#house body
def house(x,y,z):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color(z)
    t.begin_fill()
    for i in range(2):
        t.forward(200)
        t.left(90)
        t.forward(150)
        t.left(90)
    t.end_fill()
    
def roop(x,y):
    t.penup()
    t.goto(x,y)
    t.color('red')
    t.pendown()
    t.begin_fill()
    for i in range(3):
        t.fd(250)
        t.left(120)
    t.end_fill()
    
def door(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.pensize(4)
    t.color('black','brown')
    t.begin_fill()
    for i in range(4):
        t.fd(35)
        t.left(90)
        t.fd(60)
        t.left(90)
    t.end_fill()
  
#roof
def roof(x,y,z):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color(z)
    t.begin_fill()
    t.forward(230)
    t.left(140)
    t.forward(150)
    t.left(80)
    t.forward(150)
    t.left(140)
    t.end_fill()
    
    
#handle
def doorhandle(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color('white')
    t.begin_fill()
    t.circle(2)
    t.fd(7)
    t.end_fill()


# window
def windows(x,y):
    t.pu()
    t.goto(x,y)
    t.pd()
    t.color('red','white')
    t.begin_fill()
    for i in range(4):
        t.fd(20)
        t.lt(90)
        for i in range(4):
            t.fd(10)
            t.left(90)
    t.end_fill()

#car
def car(x,y):
    t.setheading(0)
    t.pensize(4)
    t.color('yellow')
    t.fillcolor('yellow')
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    
    t.fd(150)
    t.lt(90)
    t.fd(30)
    t.lt(90)
    t.fd(150)
    t.lt(90)
    t.fd(30)
    t.left(90)
    t.fd(30)
    t.right(90)
    t.circle(10)
    t.lt(90)
    t.fd(70)
    t.right(90)
    t.circle(10)
    t.left(180)
    t.fd(50)
    t.left(90)
    t.fd(70)
    t.lt(90)
    t.fd(22)
    t.lt(90)
    t.fd(37)
    t.lt(90)
    t.fd(22)
   # carspeed=2
   # for i in range(800):
    #    (x,y) = carspeed.pos(carspeed+1)

  
    t.end_fill()
    
    
def trees(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color('brown')
    t.begin_fill()
    def branch(blen):
    	if blen > 10:
    		angle = 30
    		t.pensize (blen/10)
    		t.fd(blen)
    		t.left(angle)
    		branch(blen * 0.7)
    		t.right(angle * 2)
    		branch(blen * 0.7)
    		t.left(angle)
    		t.backward(blen)
    branch(100)
    t.end_fill()
    
    
t.hideturtle()