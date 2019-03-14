import sys
inputfile=sys.argv[1]
file=open("HouseData.txt","r")

bulletList=[lines.replace("\n", "").split(" ") for lines in file.readlines()]
print(bulletList)
resultList=[]


def calculateTotalCost(bulletList):
    for item in bulletList:
        total_cost=int(item[0]) + (int(item[1]) * 10) + (int(item[0]) * float(item[2]) * 10)
        resultList.append(total_cost)
    return resultList


def displayCosts(list):
    s = 0
    displayList=calculateTotalCost(list)
    print("The total cost of each house:")
    for item in displayList:
            s+=1
            print(s,".House's total cost is ", item)


def selectBestBuy(list):
    s=0
    BestBuyList=calculateTotalCost(list)
    low=int(BestBuyList[0])
    for i in BestBuyList:
        s += 1
        if i in BestBuyList:
            if i<low:
                low=i
                print("You should select",s,".house whose total cost is",low)


displayCosts(bulletList)
selectBestBuy(bulletList)


file.close()
