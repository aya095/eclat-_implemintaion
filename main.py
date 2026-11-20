import pandas as pd 
from data_preprocessing import data_process

data = pd.read_excel("Horizontal_Format.xlsx")
  
RES=(data_process(data))
for itm in RES:
  print (itm.name,itm.support,itm.transactions)
