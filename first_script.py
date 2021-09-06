import fun as fu
print(__name__)
print(fu.__name__)
fact_list =[]
score=[45,78,4,90,2,12,9,23,54,67]
Average =fu.mean(score)
add_fivee= fu.add_five(score)
print('mean =',Average,'\n','five addition= ', add_fivee)

import math as ma
import datetime as dt
for i in score:
    if i < 50:
        print('num_fact = ',fact_list.append(ma.factorial(i)))
print(dt.datetime(2020,7,13))
