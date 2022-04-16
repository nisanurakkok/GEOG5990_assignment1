# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 16:34:43 2022

@author: student 201566838
"""
# importing modules
import matplotlib.pyplot
import agentframework #importing function defintions 
import environment #importing and reading defintion of the environment
import matplotlib.animation
import matplotlib
import tkinter
matplotlib.use('TkAgg') 
import requests
import bs4

# getting data from html link
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_xs = soup.find_all(attrs={"class" : "x"})
td_ys = soup.find_all(attrs={"class" : "y"})
# print(td_ys)
# print(td_xs) 

#setting variables
agents = []
num_of_agents = 10  #setting number of agents
num_of_iterations = 10 #setting number of interations
neighbourhood= 5
# predators = [] #creating another variable
# num_of_predators = 1

#read environment
env = environment.reading()  #reading in points of the (background) environment that is reading a CSV file

fig = matplotlib.pyplot.figure(figsize=(5,5)) #setting the defult size of the model window that it opens up as

#Looping agent initalisation, x and y set to the coordiates in the html 
for i in range(num_of_agents):
    x = int(td_xs[i].text)* 3 #increased by 3 to fit scale
    y = int(td_ys[i].text)* 3
    agents.append(agentframework.Agent(env, i, agents, x, y)) #adding to the string


#clearing after frame 
def update(frame_number):
    fig.clear() 
    
#simulating and running variables from the class 
    for i in range(num_of_agents):
         if agents[i].age >= 0 and agents[i].age <= 60: # functions move, aged, eat, waste and share with neighbour is will be active as well as age is between 0 and 60.
          agents[i].move()
          agents[i].aged()
          agents[i].eat()
          agents[i].waste()
          agents[i].share_with_neighbours(neighbourhood)
         else: agents[i].die()  #all agents will 'die' and stop all other functions will stop applying
         # print (agents[i].share_with_neighbours())
 
#plotting the graph in matplotlib.pyplot
    for i in range(num_of_agents):
        matplotlib.pyplot.xlim(0, 300) #defining the grid, x, y and title
        matplotlib.pyplot.ylim(0, 300) 
        matplotlib.pyplot.title("Environment and Agents")
        matplotlib.pyplot.xlabel("X axis")
        matplotlib.pyplot.ylabel("Y axis")
        if (agents[i].alive): # setting the colour and size of the agents 
            matplotlib.pyplot.scatter(agents[i].x,agents[i].y, c="pink",s=agents[i].store) #if agents are alive=True, they are pink
        else:
            matplotlib.pyplot.scatter(agents[i].x,agents[i].y, c="orange",s=agents[i].store) #if agents are not alive, alive=false and are the Die function, they are orange 
        matplotlib.pyplot.imshow(env) #showing, plotting the environment (background)
        # print(agents[i]) # print id, x, y, age, store
    
# for l in range(num_of_predators):
#            matplotlib.pyplot.scatter(predators[i].x, predators[i].y, c="red", s=2)
#            matplotlib.pyplot.imshow()
    
def run(): #setting up the run function
    animation = matplotlib.animation.FuncAnimation(fig, update, interval= 1, frames= num_of_iterations) #setting up and running the animation, calling in previous functions and variables that have been alread set
    canvas.draw() #intialing the plot for tkinter
    
root = tkinter.Tk() #building the main window, before the canvas.draw plots the environment and agents
menu = tkinter.Menu(root) #adding a menu bar to  window
root.config(menu=menu)
model_menu = tkinter.Menu(menu) 
menu.add_cascade(label="Run Model", command=run) #setting button and function into tkinter window to run model when clicked
root.wm_title("Environment and Agents") #title for the window
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1) 

tkinter.mainloop()   #running the tkinter event loop

