import matplotlib.pyplot as mlt
import random


mlt.pie(
    x = [100 , 200 , 150 , 400 ] , 
    explode = (0 ,  0, 0 , 0.1 ) , 
    labels = ["C++" , "Java" , "Haskell" , "Python"]  , 
    colors = ["orange" , "lightgreen" , "deeppink" , "cyan"] , 
    shadow = 1 , 
    labeldistance =  1.1 , 
    startangle = 0 , 
    counterclock = True ,  
)
mlt.legend(loc = "upper right")
mlt.show()