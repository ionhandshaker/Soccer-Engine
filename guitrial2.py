# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 02:21:40 2016

@author: Nandhakishore
"""
"""
from Tkinter import Tk,Frame,Canvas,BOTH
class Example(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent)
        self.parent=parent
        self.initUI()
        
    def initUI(self):
        self.parent.title("Lines")
        self.pack(fill=BOTH, expand=1)
        canvas=Canvas(self)
        #canvas.create_line(30,25,200,25)
        canvas.create_rectangle(30,30,550,550,fill='green')
        canvas.create_oval(140,140,150,150,fill='red')
        canvas.create_line(30,30,260,260,fill='white')
        canvas.pack(fill=BOTH, expand=1)

def main():
  
    root = Tk()
    ex = Example(root)
    root.geometry("650x650")
    root.mainloop()  


if __name__ == '__main__':
    main()  
"""

from Tkinter import *

master = Tk("Engine")

w = Canvas(master, width=670, height=670)
w.pack()

#w.create_line(0, 0, 200, 100)
#w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))

w.create_rectangle(0, 0, 420, 660, fill="green") #main field
w.create_oval(150,270,270,390,outline='white',width=2) #centre circle
w.create_line(0,330,420,330,fill='white',width=2) #half line
#w.create_oval(10,10,20,20,fill='red')
w.create_line(90,102,330,102,fill='white',width=2) #computer d box horizontal line
w.create_line(90,0,90,102,fill='white',width=2) #computer d box vertical line 1
w.create_line(330,0,330,102,fill='white',width=2) #computer d box vertical line 2
w.create_line(150,40,270,40,fill='white',width=2) #computer goal box horizontal line
w.create_line(150,0,150,40,fill='white',width=2)
w.create_line(270,0,270,40,fill='white',width=2)

#####
w.create_line(90,558,330,558,fill='white',width=2) #your d box horizontal line
w.create_line(90,660,90,558,fill='white',width=2) #your d box vertical line 1
w.create_line(330,660,330,558,fill='white',width=2) #your d box vertical line 2
w.create_line(150,620,270,620,fill='white',width=2)
w.create_line(150,660,150,620,fill='white',width=2)
w.create_line(270,660,270,620,fill='white',width=2)


#w.create_oval(270,270,280,280,fill='red')




#mainloop()

class Team:
    def __init__(self,name):
        self.name=name
        self.players=[]
        self.player_names=[]
    def add_player(self,player_var):
        self.players.append(player_var)
    def find_player_names(self):
        self.player_names=[self.players[i].name for i in range(0,len(self.players))]
        return self.player_names
    
        

class Player:
    def __init__(self,name):
        self.name=name
        self.shoot=None
        self.dribble=None
        self.passing=None
        self.defense=None
        self.icon=None
    def add_shoot(self,shoot_value):
        self.shoot=shoot_value
    def add_dribble(self,dribble_value):
        self.dribble=dribble_value
    def add_passing(self,passing_value):
        self.passing=passing_value
    def add_defense(self,defense_value):
        self.defense=defense_value
    def add_icon(self,icon_item):
        self.add_icon=icon_item


        
player1=Player("DeGea")
player2=Player("Fellaini")
player1.add_shoot(45)
player1.add_dribble(54)
player1.add_passing(67)
player1.add_defense(90)

"""
team1=[]
team1.append(player1)
team1.append(player2)
names=[team1[i].name for i in range(0,len(team1))]
"""

team1=Team("ManUtd")
team1.add_player(player1)
team1.add_player(player2)
req=team1.find_player_names()
 
if(player1.defense-player1.shoot>=30):
    item1=w.create_oval(20,20,30,30,fill='red',tag='player1')

player1.add_icon(item1)

def move_player():
    x,y=5,5
    #for i in range(2):
    #w.move(item1,x,y)
    if(w.coords(item1)[0]<310 or w.coords(item1)[1]<370):
        w.move(item1,x,y)
    print w.coords(item1)
    master.after(50,move_player)
        

b=Button(master,text='Move',command=move_player)

b.pack() 
#move_player()
mainloop()   
