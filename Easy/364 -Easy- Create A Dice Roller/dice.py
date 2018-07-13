    import random

    with open('input.txt', 'r') as f:
    	rolls = [(line.strip()).split('d')
    		for line in f.readlines()
    		if len((line.strip()).split('d'))>0]
    f.closed

    rollResult = []
    for i in range(0,len(rolls)):
        tempRollList = []
        for j in range(0,int(rolls[i][0])):
            tempRollList.append(random.randint(1,int(rolls[i][1])))
        rollResult.append(tempRollList)

    for i in range(0,len(rollResult)):
        print("{}: {}".format(sum(rollResult[i]),rollResult[i]))
    
