import csv

#function to read in for model.py as it reongises the data within the file rather than just a file 
def reading():
    """
    reading in the environment documentation 

    Returns
    -------
    environment : TYPE
        DESCRIPTION.

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

    for value in row:
        rowlist.append(value)
        #print (value) 