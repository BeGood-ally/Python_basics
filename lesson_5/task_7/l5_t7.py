from functools import reduce
import json

firms = open('l5_t7.txt', 'r')
dic_firms = {}
duc_firms = [1, 0, -4, 3]
for line in firms:
    dic_firms[line.split()[0]] = int(line.split()[2]) - int(line.split()[3])
dic_firms['income'] = reduce(lambda x,y: x + y, filter(lambda x: x > 0, dic_firms.values()))
with open("l5_t7.json", "w") as dic_firms_jsn:
    json.dump(dic_firms, dic_firms_jsn)



