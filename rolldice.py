#Import pertinent libraries
import random
import statistics
from matplotlib import pyplot as pp
from tkinter import *
import numpy as np
import pandas as pd

nrolls = 20000
sides = [4,5,5,6,6,6,7,7,7,7,8,8,8,9,9,10]
# sides = [1,2,3,4,5,6]
nsides = 6#len(sides)

rolls = []
def roll_many(n, x,numbers=[]):
    '''n is the number of sides. x is the number of rolls'''
    for i in range(x):
        if len(numbers) == 0:
            roll = random.randint(1,n)
        else:
            roll = random.choice(numbers)
        rolls.append(roll)


roll_many(nsides,nrolls,sides)


#You can check the statistics of your rolls using the statistics library
print("Number of rolls: {}; number of sides: {}".format(nrolls,nsides))
print("mean: {}".format(statistics.mean(rolls)))

print("sigma: {}".format(statistics.stdev(rolls)))

nbins = nsides
bins = np.arange(min(sides),max(sides)+2)
fig, ax = pp.subplots()
n,bins,patches = ax.hist(rolls,bins=bins,color='green',edgecolor='white',align="left")

df = pd.dataframe()


pp.xlabel("Roll")
pp.ylabel("Occurances")
pp.savefig('plot.png')



# Create the window

#The Tk() function sets up the application object
# window = Tk()
#
# #Set the window title
# window.title('Dice Roller')
#
# #Size and position of window: window.geometry("widthxheight+XPOS+YPOS")
# window.geometry("500x300+10+20")
#
# #Event listening loop
# window.mainloop()
#
#
#
#
# window=Tk()
# mywin=MyWindow(window)
# window.title('Dice Roller')
# window.geometry("400x300+10+10")
# window.mainloop()
