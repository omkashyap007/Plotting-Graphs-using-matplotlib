import random
import matplotlib.pyplot as  mlt

x =  [i for i in range(1,11)]
y =  [i for i in range(1,11)]

mlt.subplot(2,2,1)
mlt.bar(
    x = x , 
    height = y , 
    linewidth = 1 , 
    edgecolor = "aqua" , 
    color = "yellow" , 
    alpha = 1 , 
    align =  "center" ,
    bottom = 0 ,  
)
mlt.title("Bar Chart")

mlt.subplot(2,2,2)
mlt.scatter(
    x = x  , 
    y = y , 
    s = 10 , 
    c  = (1,0,0) , 
    linewidth = 1 , 
    edgecolor   =  (1,1,0)  ,     
)

mlt.subplot(2,2,3)
mlt.pie(
    x = x, 
    labels = [i for i in  "abcdefghij"] , 
    explode = (list(0 if  i<10 else 0.3  for  i  in range(1,11)) ),
)

mlt.subplot(2,2,4)
mlt.hist(
    x = [random.randint(1,50)   for _ in range(1  , 50 )] ,
    bins =[i for i in range(5, 51, 5)]  ,
    histtype  = "stepfilled"  , 
    rwidth = 1,
    color = (1,0,0,1),
    edgecolor = (1,1,0 ,1) , 
    label = "Something" , 
    linewidth = 1 ,  
)

mlt.savefig(
    fname = "plots/first.png" ,
    dpi=500 ,
    facecolor = "w",
    edgecolor = "r", 
    orientation =  "landscape" ,
    format = "png" , 
    transparent  = False 

)
mlt.show()