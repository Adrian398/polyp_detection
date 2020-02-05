import pandas as pd
import numpy as np
import re


#with open('annotation3.txt', 'r') as file:
#    data = file.read()



#data = re.sub(r'\n[0-9]+,', '\n', data)
#print(data)
#with open('annotation3.txt', 'w') as file:
#    file.write(data)

with open('annotation3.txt', 'r') as file:
    with open('annotation.txt', 'a') as file2:
        for line in file:
            line = "Original_jpg/"+ line
            file2.write(line)

    #with open('annotation3.txt', 'w') as file:
#    file.write(data)