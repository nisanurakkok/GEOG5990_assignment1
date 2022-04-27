
import csv

#function to read in for model.py as it reongises the data within the file rather than just a file 
def reading():
    """

    Returns
    -------
    environment : int
        reading in csv file which is the environment the agents will interact with.

    """
    environment = []
    with open('variable data.csv', newline='') as f:
        reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
        for row in reader:
            rowlist = []
            for value in row:
               # print(value) 
                rowlist.append(value)
            environment.append(rowlist)

    return environment

