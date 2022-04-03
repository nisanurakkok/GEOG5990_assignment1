# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 16:34:43 2022

@author: studeny 20516636
"""
import random

# class predator:
#     def __init__(self, environment, predators, x, y):
#         self.x = random.randint(0, 300)
#         self.y = random.randint (0, 300)
#         self.environment = environment
#         self.predators = predators
         

#Making the agent class
class Agent:

    # initializes the attributes of the class  object 
    def __init__ (self, environment, ia, agents, x, y):
    # binding an attribute to a given arguments
        self.environment = environment
        self.store = 0 
        self.agents = agents
        self.age = random.randint(0,20)
        self.id = ia
        self.alive = True
        if (x == None):
            self.x = random.randint(0,100)
        else:
            self.x = x 
        if (y == None):
              self.y = random.randint(0,100)
        else:
            self.y = y
 
# defining the attributes as a string, setting the layout to how the id and coordiates are printed
    def __str__(self):
        return "id" + str(self.id) +",x=" + str(self.x) +",y=" + str(self.y) +",age" + str(self.age) + ",store" + str(self.store)
    
#setting the agents to move by 2 using the random.random genertor
    def move(self): 
            if random.random() <0.5:
                self.x =(self.x +2) % 299 
            else: 
                self.x =(self.x -2) % 299
            
            if random.random() <0.5:
                self.y =(self.y +2) % 299
            else: 
                self.y =(self.y -2) % 299
                
                
# Telling die function to stop agents where they are               
    def die(self): #the agents will stay where they are and they will no longer fulfill the Alive attruibute
        self.x = self.x
        self.y = self.y
        self.alive = False
             
#setting an eat function where from the environment agents will take it and add to thier store   
    def eat(self): 
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 20
            self.store +=10 
            
#setting a waste function, where once they meant the store requirement they will add to the environment and there store will decrease
    def waste(self):
        if self.store >10:
            self.environment[self.y][self.x] +=10
            self.store -=7

#setting an age function, where age increases by 1 each iteration
    def aged(self):
          self.age += 1
         
#calculating distance between agents    
    def distance_between(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5 
              
#Looping agents in self.agents
    def share_with_neighbours(self, neighbourhood): #sharing and equaling agents to have the same store share with its neighbours
         for agent in self.agents:
            
            if self.id != agent.id:
             dist = self.distance_between(agent)
             #calculations for 'share', when 'distance between' is less than or eqaul neighbourhood (which is set)
             if dist <= neighbourhood:
                 sum = self.store + agent.store
                 ave = sum /2
                 self.store = ave
                 agent.store = ave
                 #print("share " + str(dist) + " " + str(ave))
    

    
