# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 10:05:05 2016

@author: Nandhakishore
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 07:34:55 2016

@author: Nandhakishore
"""

"""
Created on Thu Mar 24 14:44:54 2016

@author: Nandhakishore
"""
#import random as rand


from Tkinter import *
import random as rand
import time
#import sys
#sys.setrecursionlimit(20000)


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
    def find_player_shoot(self):
        self.player_shoot=[self.players[i].shoot for i in range(0,len(self.players))]
        return self.player_shoot
    def find_player_defense(self):
        self.player_defense=[self.players[i].defense for i in range(0,len(self.players))]
        return self.player_defense
    
        

class Player:
    def __init__(self,name):
        self.name=name
        self.shoot=None
        self.dribble=None
        self.passing=None
        self.defense=None
        self.icon=None
        self.orig_position=None
        self.region=None
    def add_shoot(self,shoot_value):
        self.shoot=shoot_value
    def add_dribble(self,dribble_value):
        self.dribble=dribble_value
    def add_passing(self,passing_value):
        self.passing=passing_value
    def add_defense(self,defense_value):
        self.defense=defense_value
    def move_player(self):
        x1=w.coords(self.icon)[0]
        y1=w.coords(self.icon)[1]
        x2=rand.randint(self.region[0],self.region[1])
        y2=rand.randint(self.region[2],self.region[3])
        x,y=(x2-x1)/self.dribble,(y2-y1)/self.dribble
    #x,y=x2-x1,y2-y1
        if(w.coords(self.icon)[0]<x2 or w.coords(self.icon)[1]<y2):
            w.move(self.icon,x,y)
        master.after(500,self.move_player)
        
#    #x,y=5,5
#    #for i in range(2):
#    #w.move(item1,x,y)
#    #w.itemconfig(item1,state=NORMAL)
#    #if(w.coords(red_player[10].icon)[0]<310 or w.coords(red_player[10].icon)[1]<370):
#        x1=w.coords(self.icon)[0]
#        y1=w.coords(self.icon)[1]
#        x2=rand.randint(self.region[0],self.region[1])
#        y2=rand.randint(self.region[2],self.region[3])
#        x,y=(x2-x1)/self.dribble,(y2-y1)/self.dribble
#    #x,y=x2-x1,y2-y1
#        if(w.coords(self.icon)[0]<x2 or w.coords(self.icon)[1]<y2):
#            w.move(self.icon,x,y)

    #def add_icon(self,icon_item):
     #   self.add_icon=icon_item



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
    
red_player=initialize_players(5,3,2)
blue_player=initialize_players(4,4,2)
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

red_player=initialize_skills(5,3,2,red_player)
blue_player=initialize_skills(4,4,2,blue_player)
#for formation 4,4,2
#a=4
#b=5
#c=1

def initialize_positions(a,b,c,player,half):
    #item=[]
    for i in range(11):
        if(i==0):
            
        #x=rand.randint(195,205)
            x=200
        #y=rand.randint(10,20)
            if(half=='UPPER'):
                y=15
            else:
                y=660-15
    
        if(i>=1 and i<=a):
            if(half=='UPPER'):
                y=rand.randint(100,120)
            else:
                y=660-rand.randint(100,120)
            reg=420/a
            x=((i-1)*reg+i*reg)/2
    
        if(i>=a+1 and i<=a+b):
            if(half=='UPPER'):
                y=rand.randint(220,230)
            else:
                y=660-rand.randint(220,230)
            reg=420/b
            x=((i-(a+1))*reg+(i-a)*reg)/2
        #y=222
    
        if(i>=a+b+1):
            reg=120/c
            #x=rand.randint((i-8)*100,(i-7)*100)
            x=150+((i-(a+b+1))*reg+(i-(a+b))*reg)/2
            #x=rand.randint(150,270)
            if(half=='UPPER'):
                y=rand.randint(315,320)
            else:
                y=660-rand.randint(315,320)
        if(half=='UPPER'):
            itemx=w.create_oval(x,y,x+10,y+10,fill='red',state=HIDDEN)
            #print itemx
        else:
            itemx=w.create_oval(x,y,x+10,y+10,fill='blue',state=HIDDEN)
        #print itemx
        player[i].icon=itemx
        player[i].orig_position=(x,y)
        #print player[i].icon
        #item.append(itemx)
    return player

red_player=initialize_positions(5,3,2,red_player,'UPPER')
blue_player=initialize_positions(4,4,2,blue_player,'LOWER')

#For testing purposes. Delete this part later
#req_item=w.create_oval(70,70,80,80,fill='blue')
#print req_item
#red_player[0].add_icon(req_item)
#print red_player[0].icon

def player_regions(a,b,c,player,half):
    for i in range(11):
        if(i==0):
            x1=90
            x2=330
            if(half=='UPPER'):
                y1=0
                y2=120
            else:
                y1=558
                y2=660
        if(i>=1 and i<=a):
            x1=0
            x2=420
            if(half=='UPPER'):
                y1=120
                y2=330
            else:
                y1=300
                y2=558
        if(i>=a+1 and i<=a+b):
            x1=0 
            x2=420
            if(half=='UPPER'):
                y1=300
                y2=550
            else:
                y1=120
                y2=300
        if(i>=a+b+1):
            x1=0
            x2=420
            if(half=='UPPER'):
                y1=550
                y2=660
            else:
                y1=0
                y2=120
        player[i].region=(x1,x2,y1,y2)
    return player

red_player=player_regions(5,3,2,red_player,'UPPER')
blue_player=player_regions(4,4,2,blue_player,'LOWER')
    
def start_moving():
    for i in range(11):
        red_player[i].move_player()
        blue_player[i].move_player()




#red_player[10].region=(210,420,400,660)


def display_player_initial_position():
    for i in range(11):
        w.itemconfig(red_player[i].icon,state=NORMAL)
        #w.place(x=red_player[i].orig_position(0),y=red_player[i].orig_position(1))
        #w.coords(red_player[i].icon,(red_player[i].orig_position[0],red_player[i].orig_position[1],red_player[i].orig_position[0]+10,red_player[i].orig_position[1]+10))
        w.itemconfig(blue_player[i].icon,state=NORMAL)
        #print 'Hello'
"""
def display_possession():
    #possession=rand.choice([0,1,2,3,4])
    w.itemconfig(blue_player[possession].icon,width=3)
    master.after(500,display_possession)
"""


"""
def move_player():
    #x,y=5,5
    #for i in range(2):
    #w.move(item1,x,y)
    #w.itemconfig(item1,state=NORMAL)
    #if(w.coords(red_player[10].icon)[0]<310 or w.coords(red_player[10].icon)[1]<370)
    x1=w.coords(red_player[10].icon)[0]
    y1=w.coords(red_player[10].icon)[1]
    x2=rand.randint(red_player[10].region[0],red_player[10].region[1])
    y2=rand.randint(red_player[10].region[2],red_player[10].region[3])
    x,y=(x2-x1)/red_player[10].dribble,(y2-y1)/red_player[10].dribble
    #x,y=x2-x1,y2-y1
    if(w.coords(red_player[10].icon)[0]<x2 or w.coords(red_player[10].icon)[1]<y2):
        w.move(red_player[10].icon,x,y)
    #print w.coords(item1)
    master.after(50,move_player)
"""
"""
def move_player():
    #x,y=5,5
    #for i in range(2):
    #w.move(item1,x,y)
    #w.itemconfig(item1,state=NORMAL)
    #if(w.coords(red_player[10].icon)[0]<310 or w.coords(red_player[10].icon)[1]<370)
    for i in range(200):
        x1=w.coords(red_player[10].icon)[0]
        y1=w.coords(red_player[10].icon)[1]
        x2=rand.randint(red_player[10].region[0],red_player[10].region[1])
        y2=rand.randint(red_player[10].region[2],red_player[10].region[3])
        x,y=(x2-x1)/red_player[10].dribble,(y2-y1)/red_player[10].dribble
    #x,y=x2-x1,y2-y1
        if(w.coords(red_player[10].icon)[0]<x2 or w.coords(red_player[10].icon)[1]<y2):
            w.move(red_player[10].icon,x,y)
    #print w.coords(item1)
    master.after(100,move_player)
"""

#red_player[10].move_player()
"""
def place_player():
    for i in range(200):
        red_player[10].move_player()
    master.after(100,place_player)
"""
"""  
w.itemconfig(blue_player[10].icon,width=3)
"""
        
red_team=Team("Red Team")
red_team.add_players(red_player)
blue_team=Team("Blue Team")
blue_team.add_players(blue_player)

b=Button(master,text='Initialize',command=display_player_initial_position)  
b.place(x=500,y=500)

b1=Button(master,text='Move',command=start_moving)
#b.place(relx=1,x=-2,y=2)
#b.grid(row=0, column=0, columnspan=2)
#b.pack() 
b1.place(x=600,y=600)



mainloop()



def red_error_function(team1,team2,possession):
    #defense_array=team1.find_player_defense()
    #shoot_array=team2.find_player_shoot()
    #x2=w.coords(red_player[10].icon)[0]
    #y2=w.coords(red_player[10].icon)[1]
    #for i in range()
    #main_marksman=defense_array.index(max(defense_array[1:6]))
    #defender_array=defense_array[1:6]
    #striker_array=shoot_array[6:11]
    #sorted(defender_array,reverse=True)
    #sorted(striker_array,reverse=True)
    
    out=[]
    for j in range(0,len(defense_array)):
        #x1=w.coords(team1.players[defense_array.index(defender_array[j])].icon)[0]
        #y1=w.coords(team1.players[defense_array.index(defender_array[j])].icon)[1]
        x1=w.coords(team1.players[j].icon)[0]
        y1=w.coords(team1.players[j].icon)[1]
        #x3=w.coords(team2.players[shoot_array.index(striker_array[j])].icon)[0]
        #y3=w.coords(team2.players[shoot_array.index(striker_array[j])].icon)[1]
        x3=w.coords(team2.players[possession].icon)[0]
        y3=w.coords(team2.players[possession].icon)[1]
        dist=((x3-x1)**2+(y3-y1)**2)**0.5
        out.append(dist)
    return out
    
def blue_error_function(team1,team2,possession):
    #defense_array=team1.find_player_defense()
    #shoot_array=team2.find_player_shoot()
    #x2=w.coords(red_player[10].icon)[0]
    #y2=w.coords(red_player[10].icon)[1]
    #for i in range()
    #main_marksman=defense_array.index(max(defense_array[1:6]))
    #defender_array=defense_array[1:6]
    #striker_array=shoot_array[6:11]
    #sorted(defender_array,reverse=True)
    #sorted(striker_array,reverse=True)
    
    out=[]
    for j in range(0,len(defense_array)):
        #x1=w.coords(team1.players[defense_array.index(defender_array[j])].icon)[0]
        #y1=w.coords(team1.players[defense_array.index(defender_array[j])].icon)[1]
        x1=w.coords(team2.players[j].icon)[0]
        y1=w.coords(team2.players[j].icon)[1]
        #x3=w.coords(team2.players[shoot_array.index(striker_array[j])].icon)[0]
        #y3=w.coords(team2.players[shoot_array.index(striker_array[j])].icon)[1]
        x3=w.coords(team1.players[possession].icon)[0]
        y3=w.coords(team1.players[possession].icon)[1]
        dist=((x3-x1)**2+(y3-y1)**2)**0.5
        out.append(dist)
    return out




#distances=error_function(red_team,blue_team)
#gbest=
red_defense_array=red_team.find_player_defense()
#defender_array=defense_array[1:6]
red_x1=w.coords(red_team.players[red_defense_array.index(max(red_defense_array))].icon)[0]
red_y1=w.coords(red_team.players[red_defense_array.index(max(red_defense_array))].icon)[1]
red_ball_position_x=w.coords(blue_player[10].icon)[0]
red_ball_position_y=w.coords(blue_player[10].icon)[1]
gbest_red=((red_x1-red_ball_position_x)**2+(red_y1-red_ball_position_y)**2)**0.5
#req_out=error_function(red_team,blue_team)
#possession=10

blue_defense_array=blue_team.find_player_defense()
#defender_array=defense_array[1:6]
blue_x1=w.coords(blue_team.players[blue_defense_array.index(max(blue_defense_array))].icon)[0]
blue_y1=w.coords(blue_team.players[blue_defense_array.index(max(blue_defense_array))].icon)[1]
blue_ball_position_x=w.coords(blue_player[10].icon)[0]
blue_ball_position_y=w.coords(blue_player[10].icon)[1]
gbest_blue=((blue_x1-blue_ball_position_x)**2+(blue_y1-blue_ball_position_y)**2)**0.5

#while True:
possession=rand.choice([ch for ch in range(11)])
w.itemconfig(blue_player[possession].icon,width=3)
    #time.sleep(0.1)
count=0
pbestred=red_error_function(red_team,blue_team,possession)
pbestblue=blue_error_function(red_team,blue_team,possession)
while count<10000:
    possession=rand.choice([ch for ch in range(11)])
        #w.itemconfig(blue_player[possession].icon,width=3)
    coin=rand.choice([0,1])
    if(coin==1):
        red_req_out=red_error_function(red_team,blue_team,possession)
        for k in range(11):
            if(red_req_out[k]>pbestred[k]):
                pbestred[k]=red_req_out[k]
    else:
        blue_req_out=blue_error_function(red_team,blue_team,possession)
        for k in range(11):
            if(blue_req_out[k]>pbestblue[k]):
                pbestblue[k]=blue_req_out[k]
    #def display_possession():
        #possession=rand.choice([0,1,2,3,4])
    
    #time.sleep(0.5)
    #master.after(500,display_possession)

    #w.itemconfig(blue_player[possession].icon,width=3)
    #display_possession(possession)
    #master.after(500,w.itemconfig(blue_player[possession].icon,width=3))
    #k=150
    if(coin==1):
        if(min(red_req_out))<gbest_red:
            gbest_red=min(red_req_out)
            main_defender=req_out.index(min(red_req_out))
            for x in range(11):
                k=gbest_red-red_req_out[x]+pbestred[x]+red_req_out[x]
            #red_player[x].region=(red_player[x].region[0]-k,red_player[x].region[1]-k,red_player[x].region[2]-k,red_player[x].region[3]-k)
                if(w.coords(blue_player[possession].icon)[1]>w.coords(red_player[x].icon)[1]):
                    red_player[x].region=(red_player[x].region[0]-k,red_player[x].region[1]-k,red_player[x].region[2]-k,red_player[x].region[3]-k)
                else:
                    red_player[x].region=(red_player[x].region[0]+k,red_player[x].region[1]+k,red_player[x].region[2]+k,red_player[x].region[3]+k)
    else:
        if(min(red_req_out))<gbest_blue:
            gbest_blue=min(blue_req_out)
            main_defender=req_out.index(min(blue_req_out))
            for x in range(11):
                k=gbest_blue-blue_req_out[x]+pbestblue[x]+blue_req_out[x]
            #red_player[x].region=(red_player[x].region[0]-k,red_player[x].region[1]-k,red_player[x].region[2]-k,red_player[x].region[3]-k)
                if(w.coords(red_player[possession].icon)[1]>w.coords(blue_player[x].icon)[1]):
                    blue_player[x].region=(blue_player[x].region[0]-k,blue_player[x].region[1]-k,blue_player[x].region[2]-k,blue_player[x].region[3]-k)
                else:
                    blue_player[x].region=(blue_player[x].region[0]+k,blue_player[x].region[1]+k,blue_player[x].region[2]+k,blue_player[x].region[3]+k)
        
        """
        defense_array=red_team.find_player_defense()
        shoot_array=blue_team.find_player_shoot()
        defender_array=defense_array[1:6]
        striker_array=shoot_array[6:11]
        sorted(defender_array,reverse=True)
        sorted(striker_array,reverse=True)
        for l in range(5):
            red_player[defense_array.index(defender_array[l])].region=(blue_player[shoot_array.index(striker_array[l])].region[0]-k,blue_player[shoot_array.index(striker_array[l])].region[1]-k,blue_player[shoot_array.index(striker_array[l])].region[2]-k,blue_player[shoot_array.index(striker_array[l])].region[3]-k)
        """
    count=count+1
    #w.itemconfig(blue_player[possession].icon,width=3)
    #time.sleep(0.5)




"""
b=Button(master,text='Initialize',command=display_player_initial_position)  
b.place(x=500,y=500)

b1=Button(master,text='Move',command=start_moving)
#b.place(relx=1,x=-2,y=2)
#b.grid(row=0, column=0, columnspan=2)
#b.pack() 
b1.place(x=600,y=600)
"""
#move_player(red_player[10])
#def player_regions()
#b2=Button(master,text='Start',command=start_simulation)
#b2.place(x=500,y=400)
"""
red_team=Team("Red Team")
red_team.add_players(red_player)
blue_team=Team("Blue Team")
blue_team.add_players(blue_player)
#w.itemconfig(red_team.players[10].icon,state=NORMAL)
"""
#mainloop()
