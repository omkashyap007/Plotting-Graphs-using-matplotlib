import matplotlib.pyplot as mlt
import random
import math

x_axis = [i  for i in range(1 , 51 , 5)]
print(x_axis)
y_axis = [random.randint(1,100) for _ in range(10)]
x_tick_label = [i for  i in  "abcdefghij"] 
y_tick_label = [i for i in range(5, 101 , 5)]
mlt.bar(
    x = x_axis , 
    height = y_axis , 
    color = "deeppink" , 
    width = 2 , 
    alpha = 1 , 
    linewidth  = 1 ,  
    edgecolor =  "aqua" , 
    align = "center" , 
    bottom = 0 , 
)
mlt.legend(["Yeah boi!!"] , loc = "upper right")
mlt.xlabel("The legend at the bottom") 
mlt.ylabel("The legend on the left side")
mlt.xticks(x_axis , x_tick_label)
mlt.yticks(y_tick_label)
mlt.grid(True)
mlt.show()
