import random
with open("seaborn_lib/data_set/random_seaborn_data.py" ,  "w")  as f   : 
    l = [[random.randint(1,100) for _ in range(1,11)] for _ in  range(1,11) ]
    f.write("""a = {}""".format(l))
    