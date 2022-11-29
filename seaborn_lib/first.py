import numpy as np
import pandas as pd
import matplotlib.pyplot as mlt
import random
import seaborn

seaborn.set(style= "whitegrid")
x = [random.randint(1,11)   for _ in range(20)]
y = [random.randint(1,11)   for _ in range(20)]
seaborn.boxplot(x  = x  ,y = y ,notch= True ,flierprops = {"marker"  : "x" } , 
                boxprops={"facecolor": (0,1,1,1)})
mlt.show()