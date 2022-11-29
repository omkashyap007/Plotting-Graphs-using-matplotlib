import matplotlib.pyplot as mlt
import random

x = [random.randint(1,50)for _ in range(1,11)]
print(x)

mlt.hist(
    x = x , 
    bins = [i for i in range(5 , 51 ,  5 )],
    orientation = ("vertical") , 
    cumulative = False  , 
    histtype = "stepfilled" ,
    rwidth =1 ,
    color = "yellow"  ,
    edgecolor = "red" , 
    linewidth = 5 ,
    label = ["The top bottom"] , 
    
)
mlt.xlabel("The bottom one !") 
mlt.ylabel("The left side one !")
mlt.legend(["Something about the hist"] , loc = "upper left")
mlt.show()