import matplotlib.pyplot as mlt
import random

mlt.scatter(
    x = [i for i in range(1,101)] , 
    y = [random.randint(1,200 ) for _ in range(1,101)],  
    s = 50 , 
    c = (160/255 , 140/255 , 240/255) ,
    alpha = 1 , 
    linewidth = 2 , 
    edgecolors  = [(random.randint(0,255)/255 , random.randint(0,255)/255 ,random.randint(0,255)/255) for _ in range(100)],    
)
mlt.grid()
mlt.xlabel("The bottom one !") 
mlt.ylabel("The left side one !")
mlt.yticks([i  for  i in range(0   ,  201 ,  5)])
mlt.grid()
mlt.legend(["points"] , loc = "upper right")
mlt.show()
