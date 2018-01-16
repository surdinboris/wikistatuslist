import re
import os

debug=False


tmplt=open(os.path.join(os.getcwd(),'_template.txt'),'r', encoding="utf-8")
outptmplt=open(os.path.join(os.getcwd(),'_otemplate.txt'),'w', encoding="utf-8")
#patterns
searchop=re.compile(r".*<todo.*>")
searchcl=re.compile(r".*</todo.*>")
counter=0
rowcollect=False

#search procedure
match=lambda x,y: x.match(y) if x.match(y) else None



def rowwrite(row):
    outptmplt.write(row)

def rowexclude(row,rowtype):
#rowtypes: 1-opened and closed, 2-opened, 3-closed, 4-just a row
    if rowtype == 1 : #adding oneliner  row
        tags=str(str(counter).join((re.match(r"(<todo.*>).*?(</todo>)", row)[1],re.match(r"(<todo.*>).*?(</todo>)", row)[2])))
        tagdata=str(re.match(r"<todo.*>(.*?)</todo>", row)[1])
        rowwrite(''.join((tags,tagdata, '\n')))

    elif rowtype ==2 : #adding partial row (with opened tag)
        tags=str(str(counter).join((re.match(r"(<todo.*>).*?", row)[1], "</todo>")))
        tagdata=str(re.match(r"<todo.*>(.*)", row)[1])
        rowwrite(''.join((tags,tagdata, '\n')))
        if debug == True:
            print(''.join((tags,tagdata, '\n')))

    elif rowtype == 3: #adding row with  closed tag
        tagdata=str(re.match(r"(.*)</todo>", row)[1])
        rowwrite(''.join((tagdata, '\n')))
        if debug == True:
            print(''.join((tagdata, '\n')))
    elif rowtype == 4:
         rowwrite(''.join((row,'\n')))
    else:
        print('improper rowtype error')

def tagscollect(row):
    tagsclctr = {}
    if match(searchop,row):
        if debug == True:
            print(match(searchop,row), 'open tag in row %d' %counter )
        tagsclctr['opened'] = counter
    if match(searchcl, row):
        if debug == True:
            print(match(searchcl, row), 'closed tag in row %d' %counter )
        tagsclctr['closed'] = counter
    return tagsanalyze(row, tagsclctr)

def tagsanalyze(row,oneliner):
    if len(oneliner)== 2 and oneliner['opened'] == oneliner['closed']:
        rowexclude(row,rowtype=1)
    elif len(oneliner) == 1:
        try:
            x=oneliner['opened']
            rowexclude(row, rowtype=2)
        except KeyError:
            try:
                x = oneliner['closed']
                rowexclude(row,rowtype=3)
            except KeyError:
                print('something went wrong - weve grab some data but its nor closed and not opened tag - chexk row %s' %row)
    elif len(oneliner) == 0:
        rowexclude(row, rowtype=4)

#script init

for row in tmplt.readlines():
    counter += 1
    tagscollect(row)
tmplt.close()
outptmplt.close()