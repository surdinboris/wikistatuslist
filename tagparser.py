import re
import os
debug=False

tmplt=open(os.path.join(os.getcwd(),'cdc/','ibox1982.txt'),'r', encoding="utf-8")
searchop=re.compile(r".*<todo.*>")
tagsclctr = {}
currstation=""
counter=0

match=lambda x,y: x.match(y) if x.match(y) else None
def tagscollect(row,station):
    if match(searchop,row):
        tagstatus=re.search(r"<todo.*(#.*?>)", row)
        if tagstatus: # if job done, adding with Done status
            tagsclctr[counter] = [station,tagstatus[1] ,'Done']
        else:
            tagsclctr[counter] = 'Pending'

for row in tmplt.readlines():
    #iteration and station collecting
    station='sys10'
    counter += 1
    tagscollect(row, station)
tmplt.close()

print(tagsclctr)
