import pandas as pd 
data = pd.read_excel("Horizontal_Format.xlsx")
  
RES=(data_process(data))
for itm in RES:
  print (itm.name,itm.support,itm.transactions)
