with open('l5_t3.txt') as salary:
    wokers = []
    for line in salary:
        woker = line.split(':')
        if int(woker[1]) >= 20000:
            wokers.append(woker[0])
        else:
            continue
    print(wokers)




