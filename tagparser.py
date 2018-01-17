import re
import os
debug=False

tmplt=open(os.path.join(os.getcwd(),'cdc/','ibox1982.txt'),'r', encoding="utf-8")
searchop=re.compile(r".*<todo.*>")
tagsclctr = {}
currstation=""
counter=0
station=''
match=lambda x,y: x.match(y) if x.match(y) else None
def tagscollect(row,station):
    global counter
    if match(searchop,row): #finding only opening tags
        counter += 1
        tagstatus=re.search(r"<todo.*#(.*?):(.*?)>", row)
        if tagstatus: # analysing opening tag and if job done, adding with Done status
            tagsclctr[counter] = [station,'Done',tagstatus[1],tagstatus[2]]
        else: # analysing opening tag and if job not executed, adding with Pending status
            tagsclctr[counter] = [station,'Pending']

for row in tmplt.readlines():
    st=re.search(r"={2,}?\s(.*?)\s*={2,}", row)
    if st:
        #print(st[1])
        station=st[1]
    tagscollect(row, station)
tmplt.close()
for item in tagsclctr.items():
    print(item)
#print(tagsclctr)
