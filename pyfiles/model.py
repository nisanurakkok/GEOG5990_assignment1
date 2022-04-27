# @author: student 201566838

import matplotlib.pyplot
import agentframework #importing function defintions 
import environment #importing and reading defintion of the environment
import matplotlib.animation
import matplotlib
import tkinter
matplotlib.use('TkAgg') 
import requests
import bs4

"""getting data from html link"""
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_xs = soup.find_all(attrs={"class" : "x"})
td_ys = soup.find_all(attrs={"class" : "y"})
# print(td_ys)
# print(td_xs) 

"""setting variables"""
agents = []
num_of_agents = 10  
num_of_iterations = 10 
neighbourhood= 5
# predators = [] #creating another variable
# num_of_predators = 1

"""reading environment csv"""
env = environment.reading()  
"""setting THE default size of window"""
fig = matplotlib.pyplot.figure(figsize=(5,5)) 

"""Looping agent initalisation, x and y that are set to the coordiates in the html"""
for i in range(num_of_agents):
    x = int(td_xs[i].text)* 3 #increased by 3 to fit scale
    y = int(td_ys[i].text)* 3
    agents.append(agentframework.Agent(env, i, agents, x, y)) #adding to the string


def update(frame_number):
    """

    clearing after frame 


    """
    fig.clear() 
    
    for i in range(num_of_agents):
        """ simulating and running variables, functions move, aged, eat, waste and share with neighbour is will be active as well as age is between 0 and 60 otherwise all agents will 'die' and stop all other functions will stop applying """
        if agents[i].age >= 0 and agents[i].age <= 60: 
            agents[i].move()
            agents[i].aged()
            agents[i].eat()
            agents[i].waste()
            agents[i].share_with_neighbours(neighbourhood)
        else: agents[i].die()  
         # print (agents[i].share_with_neighbours())
 
    for i in range(num_of_agents):
        """ Plotting graph in matplotlib.pyplot"""
        matplotlib.pyplot.xlim(0, 300) 
        matplotlib.pyplot.ylim(0, 300) 
        matplotlib.pyplot.title("Environment and Agents")
        matplotlib.pyplot.xlabel("X axis")
        matplotlib.pyplot.ylabel("Y axis")
        if (agents[i].alive): 
            matplotlib.pyplot.scatter(agents[i].x,agents[i].y, c="pink",s=agents[i].store) #if agents are alive=True, they are pink
        else:
            matplotlib.pyplot.scatter(agents[i].x,agents[i].y, c="orange",s=agents[i].store) #if agents are not alive, alive=false and are the Die function, they are orange 
        matplotlib.pyplot.imshow(env) #showing, plotting the environment (background)
        # print(agents[i]) # print id, x, y, age, store
    
# for l in range(num_of_predators):
#            matplotlib.pyplot.scatter(predators[i].x, predators[i].y, c="red", s=2)
#            matplotlib.pyplot.imshow()
    
def run():
    """ Running animation, setting the number of iterations"""
    animation = matplotlib.animation.FuncAnimation(fig, update, interval= 1, frames= num_of_iterations) #setting up and running the animation, calling in previous functions and variables that have been alread set
    canvas.draw() #intialing the plot for tkinter
"""  building the main window  for GUI """
root = tkinter.Tk()
menu = tkinter.Menu(root)
root.config(menu=menu)
model_menu = tkinter.Menu(menu) 
menu.add_cascade(label="Run Model", command=run) #setting button and function into tkinter window to run model when clicked
root.wm_title("Environment and Agents") #title for the window
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1) 

tkinter.mainloop()   

