from Tkinter import *
import random as rand

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
w.create_line(90,558,330,558,fill='white',width=2) #your d box horizontal line
w.create_line(90,660,90,558,fill='white',width=2) #your d box vertical line 1
w.create_line(330,660,330,558,fill='white',width=2) #your d box vertical line 2
w.create_line(150,620,270,620,fill='white',width=2)
w.create_line(150,660,150,620,fill='white',width=2)
w.create_line(270,660,270,620,fill='white',width=2)
w.create_line(185,2,225,2,fill='black',width=2) #goal
w.create_line(185,660,225,660,fill='black',width=2)

class Team:
    def __init__(self,name):
        self.name=name
        self.players=[]
        self.player_names=[]
    def add_players(self,player_list):
        self.players=player_list
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



def initialize_players(a,b,c):
    player=[]
    for i in range(11):
        if(i==0):
            x=Player("Goalkeeper")
        if(i>=1 and i<=a):
            x=Player("Defender_%d"%i)
        if(i>=(a+1) and i<=(a+b)):
            x=Player("Midfielder_%d"%(i-a))
        if(i>=a+b+1): 
            x=Player("Striker_%d"%(i-(a+b)))
        player.append(x)
    return player
    
red_player=initialize_players(5,2,3)
#blue_player=player_initialization()
#player[0].name='Goalkeeper'

def initialize_skills(a,b,c,player):
    for i in range(11):
        if(i==0):
            p=rand.randint(90,100)
        elif(i>=1 and i<=a):
            p=rand.randint(75,90)
        else:
            p=rand.randint(1,75)
        if(i>=a and i<b):
            q=rand.randint(75,100)
            r=rand.randint(75,100)
        else:
            q=rand.randint(1,75)
            r=rand.randint(1,75)
        if(i>=b):
            s=rand.randint(75,100)
        else:
            s=rand.randint(1,75)
    #print p,q,r,s
        player[i].add_defense(p)
        player[i].add_passing(q)
        player[i].add_dribble(r)
        player[i].add_shoot(s)
    return player

red_player=initialize_skills(5,2,3,red_player)

#for formation 4,4,2
item=[]
for i in range(11):
    if(i==0):
        #x=rand.randint(195,205)
        x=200
        #y=rand.randint(10,20)
        y=660-15
    
    if(i>=1 and i<=4):
        #x=rand.randint((i-1)*100,i*100)
        y=660-rand.randint(100,120)
        x=((i-1)*100+i*100)/2
        #y=110
    
    if(i>=5 and i<=8):
        #x=rand.randint((i-5)*100,(i-4)*100)
        y=660-rand.randint(220,230)
        x=((i-5)*100+(i-4)*100)/2
        #y=222
    
    if(i>=9):
        x=rand.randint((i-8)*100,(i-7)*100)
        y=660-rand.randint(315,320)
    
    itemx=w.create_oval(x,y,x+10,y+10,fill='blue')
    red_player[i].add_icon(itemx)
    item.append(itemx)



    
red_team=Team("Red Team")
red_team.add_players(red_player)


mainloop()
