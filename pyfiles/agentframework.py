# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 16:34:43 2022

@author: student 201566838
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
    

    def __init__ (self, environment, ia, agents, x, y):
        """
        

        Parameters
        ----------
        environment : int
            Reading in data of what the environment through integers from 1 to 255.
        agents : array, int
            DESCRIPTION.
        x : float
            x coordinates for agents.
        y : float
            y coordinates for agents.

        Returns
        -------
        The attributes that are set to the class object, binding the attricbutes to a given agruments .

            """
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
 
    def __str__(self):
        """
        

        Returns
        -------
        str
            defining the attributes as a string, setting the layout to how the id and coordiates are printed.

        """
        return "id" + str(self.id) +",x=" + str(self.x) +",y=" + str(self.y) +",age" + str(self.age) + ",store" + str(self.store)
    
    def move(self): 
        """
        

        Returns
        -------
        Setting the agents to move by 2 using the random.random genertor within the environment

        """
        if random.random() <0.5:
                self.x =(self.x +2) % 299 
        else: 
                self.x =(self.x -2) % 299
            
        if random.random() <0.5:
                self.y =(self.y +2) % 299
        else: 
                self.y =(self.y -2) % 299
                
                
                
    def die(self):
        """
        

        Returns

        -------
        Telling agents to stop where they are. The false statement is when they  no longer fulfill the Alive attruibute.

        """
        self.x = self.x
        self.y = self.y
        self.alive = False
             
    def eat(self):
        """
        

        Returns
        -------
        Agents will take from the environment and add to thier own store   

        """
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 20
            self.store +=10 
            
#setting a waste function, where once they meant the store requirement they will add to the environment and there store will decrease
    def waste(self):
        """
        

        Returns
        -------
        Once agents have meant the store requirement they will add to the environment which will allow thier store to decrease

        """
        if self.store >10:
            self.environment[self.y][self.x] +=10
            self.store -=7

    def aged(self):
        """
        

        Returns
        -------
        Setting an age function, where age increases by 1 each iteration

        """
        self.age += 1
         
         
    def distance_between(self, agent):
        """
        

        Parameters
        ----------
        agent : int

        Returns
        -------
        float
        calculating distance between self and other agents    

        """
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5 
              
    def share_with_neighbours(self, neighbourhood): 
        """
        

        Parameters
        ----------
        neighbourhood : float
            
        Returns
        -------
        float 
        calcuating distance agents shares to equal the amount of store between the agents to have the same store with its neighbours 

        """
        
        for agent in self.agents:
            
            if self.id != agent.id:
             dist = self.distance_between(agent)
             if dist <= neighbourhood:
                 sum = self.store + agent.store
                 ave = sum /2
                 self.store = ave
                 agent.store = ave
                 #print("share " + str(dist) + " " + str(ave))
    

    
