import os

dirr=os.path.join(os.environ['USERPROFILE'],'AppData/Local/Google/Chrome/User Data/Default/Cache')
#print(os.listdir(dirr))
curlist=os.listdir(dirr)
while True:
    if len(os.listdir(dirr))!= len(curlist):
        print(set(os.listdir(dirr)).intersection(curlist))
        curlist=(os.listdir(dirr))

#targdir=\AppData\Local\Google\Chrome\User Data\Default\Cache