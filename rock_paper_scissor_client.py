#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 07:15:03 2019

@author: elzhar
"""

import tkinter as tk
import socket as sk
import threading as th

s=sk.socket(sk.AF_INET,sk.SOCK_STREAM)
s.setsockopt(sk.SOL_SOCKET,sk.SO_REUSEADDR, 1)
host='127.0.0.1'
port=7000
s.connect((host,port))

window = tk.Tk()
window.title('Client')
window.geometry('500x250')
lb1=tk.Label(window,text='your choice',font=('Verdana', 16))
lb1.grid(row=0,column=0,padx=(10,25),pady=(10,10))
lb2=tk.Label(window,text='opponent choice',font=('Verdana', 16))
lb2.grid(row=0,column=1,padx=(25,0),pady=(10,10))
lb3=tk.Label(window,text='Waiting...',font=('Verdana', 16))
lb3.grid(row=1,column=0,padx=(10,25),pady=(10,10))
lb4=tk.Label(window,text='Waiting...',font=('Verdana', 16))
lb4.grid(row=1,column=1,padx=(25,0),pady=(10,10))
lb5=tk.Label(window,text='',font=('Verdana', 16))
lb5.grid(row=3,column=1,pady=(10,10))

my_choice=''
opnnt_choice=''

def compare(my_choice,opnnt_choice):
    results = {('Paper','Rock') : True,
               ('Paper','Scissors') : False,
               ('Rock','Paper') : False,
               ('Rock','Scissors') : True,
               ('Scissors','Paper') : True,
               ('Scissors','Rock') : False}
    return results[(my_choice,opnnt_choice)]

def recv_func():
    while True:
        global my_choice
        global opnnt_choice
        opnnt_choice=s.recv(2048).decode('utf-8')
        if opnnt_choice=='reset':
            lb5['text']='play again'
        if opnnt_choice!='' and opnnt_choice!='reset': 
            lb4['text']='choosed'
        if my_choice!='' and opnnt_choice!='' and opnnt_choice!='reset':
           if  my_choice==opnnt_choice:
               lb5['text']='Tie!'
               lb3['text']=my_choice
               lb4['text']=opnnt_choice
           elif compare(my_choice,opnnt_choice):
               lb5['text']='You Win'
               lb3['text']=my_choice
               lb4['text']=opnnt_choice
           else:
               lb5['text']='You Lose'
               lb3['text']=my_choice
               lb4['text']=opnnt_choice

rcv_thrd=th.Thread(target=recv_func)
rcv_thrd.start()
        

def clicked1():
    global my_choice
    global opnnt_choice
    my_choice='Rock'
    s.send(my_choice.encode('utf-8'))
    lb3['text']='Rock'
    if lb4['text']=='choosed':
       if  my_choice==opnnt_choice:
           lb5['text']='Tie!'
           lb3['text']=my_choice
           lb4['text']=opnnt_choice
       elif compare(my_choice,opnnt_choice):
           lb5['text']='You Win'
           lb3['text']=my_choice
           lb4['text']=opnnt_choice
       else:
           lb5['text']='You Lose'
           lb3['text']=my_choice
           lb4['text']=opnnt_choice

def clicked2():
    global my_choice
    global opnnt_choice
    my_choice='Paper'
    s.send(my_choice.encode('utf-8'))
    lb3['text']='Paper'
    if lb4['text']=='choosed':
       if  my_choice==opnnt_choice:
           lb5['text']='Tie!'
           lb3['text']=my_choice
           lb4['text']=opnnt_choice
       elif compare(my_choice,opnnt_choice):
           lb5['text']='You Win'
           lb3['text']=my_choice
           lb4['text']=opnnt_choice
       else:
           lb5['text']='You Lose'
           lb3['text']=my_choice
           lb4['text']=opnnt_choice

def clicked3():
    global my_choice
    global opnnt_choice
    my_choice='Scissors'
    s.send(my_choice.encode('utf-8'))
    lb3['text']='Scissors'
    if lb4['text']=='choosed':
       if  my_choice==opnnt_choice:
           lb5['text']='Tie!'
           lb3['text']=my_choice
           lb4['text']=opnnt_choice
       elif compare(my_choice,opnnt_choice):
           lb5['text']='You Win'
           lb3['text']=my_choice
           lb4['text']=opnnt_choice
       else:
           lb5['text']='You Lose'
           lb3['text']=my_choice
           lb4['text']=opnnt_choice

def reset():
    s.send('reset'.encode('utf-8'))
    global my_choice
    global opnnt_choice
    my_choice=''
    opnnt_choice=''
    lb3['text']='Waiting...'
    lb4['text']='Waiting...'
    lb5['text']=''
    
btn1=tk.Button(window,text='Rock',font=('Verdana', 16),command=clicked1)
btn1.grid(row=2,column=0,pady=(10,10))
btn2=tk.Button(window,text='Paper',font=('Verdana', 16),command=clicked2)
btn2.grid(row=2,column=1,pady=(10,10))
btn3=tk.Button(window,text='Scissors',font=('Verdana', 16),command=clicked3)
btn3.grid(row=2,column=2,pady=(10,10))
btn3=tk.Button(window,text='Play Again',font=('Verdana', 16),command=reset)
btn3.grid(row=4,column=1,pady=(10,10))

window.mainloop()