# GEOG5990_assignment1
This project is an Agent-Based Model.

The model is showing agents in an envirvonmemt through matplotlib.ppyplot animation function. Overall the agents will be interating in the environment while engaing between each other and the environemnt. The model is set to start through Tkinter, which requires you to 'run model' to start the model. A more detailed read me explantion of what the model is able to do as well as any improvements and issues can be found in the website at https://nisanurakkok.github.io/GEOG5990_assignment1/.
In files you can find the website codes and links, licensing and three different pyhton files that read in environment, define function in agentframework and that run the model. You can download the python and variable data locally through the file assignment1pythonfiles. To access the sphynx please log into dialogplus server, http://dialogplus.leeds.ac.uk/geog5870/web15/pyhton/_build/agentframework.html. 

Within the model, the code:
- imports modules 
- gathers data from a html using beautiful soups 
- setting up variables
- reading in the environment, through the csv
- intilisasing x and y vaules
- running the functions
- setting the graph through Matplotlib
- using tkinter to set up GUI

Within the environment, the code:
-imports modules csv
- reads a csv and converts it, to be readable 

Within the agentframework, the code:
-imports module, random 
- sets variables 
- defines multiple functions 
  - waste (Once the agents have reached a certain store level, they will add back to the environment and where they decrease thier store)
  - str (defning the str how to print)
  - move (setting the agents to move in x or y direction by 2 wihtin the environment)
  - die (agents die where they are, when the false statement is when they  no longer fulfill the Alive attruibute.)
  - eat (agents will eat the environment, and the environment will decrease)
  - aged (the age is set through the random function at the start, the function then increases the age by one till it dies, where in the model its stop and die at 60)
  - distance between ()


This project was done under the University of Leeds, as a taught module, the author is Nisa Akkok, my Student ID is 201566838.
