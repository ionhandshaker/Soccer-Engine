
from Tkinter import *

master = Tk("Engine")

w = Canvas(master, width=670, height=670)
w.pack()


w.create_rectangle(0, 0, 420, 660, fill="green") #main field
w.create_oval(150,270,270,390,outline='white',width=2) #centre circle
w.create_line(0,330,420,330,fill='white',width=2) #half line
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
    def add_shoot(self,shoot_value):
        self.shoot=shoot_value
    def add_dribble(self,dribble_value):
        self.dribble=dribble_value
    def add_passing(self,passing_value):
        self.passing=passing_value
    def add_defense(self,defense_value):
        self.defense=defense_value


        
player1=Player("DeGea")
player2=Player("Fellaini")
player1.add_shoot(45)
player1.add_dribble(54)
player1.add_passing(67)
player1.add_defense(90)


team1=Team("ManUtd")
team1.add_player(player1)
team1.add_player(player2)
req=team1.find_player_names()
 
if(player1.defense-player1.shoot>=30):
    item1=w.create_oval(20,20,30,30,fill='red',tag='player1')
    
w.move(item1,70,70)

 
mainloop()   
        
