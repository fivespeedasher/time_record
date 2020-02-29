# coding=gbk
from pyecharts import Pie
def build_lists(a):
    dicall = {}
    tings = []
    spend = []
    num = len(a)
    for i in range(num):
        if a[i][0].isnumeric() == False:
            tings.append(a[i])
            spend.append(int(a[i+1]))
            if a[i] in dicall:
                dicall[a[i]] += int(a[i+1])
            else:dicall[a[i]] = int(a[i+1])
        else:continue
    return dicall

def build_pid(dicall):
    tings = []
    spend = []
    for key,value in dicall.items():
        tings.append(key)
        spend.append(value)
    pie = Pie(" ")
    pie.add("饼图",tings,spend,legend_orient="vertical",legend_pos="left",center=[75, 50])
    pie.render(r'C:\Users\asshole\Desktop\pie.html')

fr = open(r'C:\Users\asshole\Desktop\record .txt','r')
a = fr.read().replace("\n"," ").replace("分钟",'').split(" ")
dicall = build_lists(a)
build_pid(dicall)

fr.close()



