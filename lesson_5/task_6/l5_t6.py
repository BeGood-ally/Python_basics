import re
from functools import reduce

shedule = open('l5_t6.txt', encoding='utf-8')
shedule_summ = {}
for line in shedule:
    summ = reduce(lambda x, y: int(x) + int(y), re.findall('\d+', line))
    subj = line.split(':')[0]
    shedule_summ[subj] = int(summ)
print(shedule_summ)


