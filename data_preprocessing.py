
def data_process(data):
# print(data)
 class Item:
    def __init__(self, name):
        self.name = name
        self.transactions = []
        self.support = 0

 items_in_all = []
 for index, row in data.iterrows():
    tid = row.iloc[0]
    items =str(row.iloc[1]).split(",")
    for item in items :
       found= False
       for x in items_in_all:
         if  x.name == item :
          found =True
          if tid not in x.transactions :
            x.transactions.append(tid)
            x.support +=1
          break
       if not found :
         new =Item(item)
         new.support+=1
         new.transactions.append(tid)
         items_in_all.append(new)
          
 return items_in_all 
