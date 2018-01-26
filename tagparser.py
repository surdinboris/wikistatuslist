import re
import os
class Collector:
    def __init__(self, tmplt):
        self.debug = False
        #self.tmplt = open(os.path.join(os.getcwd(), 'cdc/', 'ibox1967.txt'), 'r', encoding="utf-8")
        self.tmplt=tmplt
        self.searchop = re.compile(r".*<todo.*>")
        self.tagsclctr = {}
        self.currstation = ""
        self.counter = 0
        self.station = ''
        self.match = lambda x, y: x.match(y) if x.match(y) else None

        self.tmplt=open(self.tmplt, 'r', encoding="utf-8")
        for row in self.tmplt.readlines():
            st = re.search(r"={2,}?\s(.*?)\s*={2,}", row)
            if st:
                if re.search(r".*reconfig.",row): #filtering unneccesary reconfig actions
                    break
                self.station = st[1]
            self.tagscollect(row, self.station)
        self.tmplt.close()
        if self.debug:
            for item in self.tagsclctr.items():
                 print(item)

    def tagscollect(self,row,station):
        if self.match(self.searchop,row): #finding only opening tags
            self.counter += 1
            tagstatus=re.search(r"<todo.*#(.*?):(.*?)>", row)
            if tagstatus: # analysing opening tag and if job done, adding with Done status
                self.tagsclctr[self.counter] = {'station':station,'status':'Done','user':tagstatus[1],'date':tagstatus[2]}
            else: # analysing opening tag and if job not finished, adding with Pending status
                self.tagsclctr[self.counter] = {'station':station,'status':'Pending','user':'','date':''}

#Example
# ct=Collector(os.path.join(os.getcwd(), 'cdc/', 'ibox1967.txt'))
# print(ct.tagsclctr)
# for f in os.listdir(os.path.join(os.getcwd(), 'cdc/')):
#     print("----------------------%s-------------------------" %f)
#     ct=Collector(os.path.join(os.getcwd(),'cdc/',f))
#     print(ct.tagsclctr)
