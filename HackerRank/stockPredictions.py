import numpy as np
from copy import copy

class Stock():
    predictedIncome = 0
    eqParams = np.array([])
    buyingValueCoef = 0
    sellingValueCoef = 0
    
    def __init__(self):
        self.xArray = np.array([1,2,3,4,5])
        
    def stackUpdate(self, name, number, history):
        self.name = name
        self.number = number
        self.history = np.array(history)
        self.quadraticFitting()
        self.predictedIncome = self.calcValueOfInvestment()
        self.checkIfTheSmallest()
        self.checkIfTheBiggest()
        
    def quadraticFitting(self):
        # print(self.history)
        # use a polyfit for that
        self.eqParams = np.polyfit(self.xArray, self.history, 2)
        
    def calcValueOfInvestment(self):
        nextDay = 6
        predictedVal = self.eqParams[0]**2 * nextDay + self.eqParams[1] * nextDay + self.eqParams[2]
        return predictedVal - self.history[-1]
    
    def checkIfTheSmallest(self):
        tmpArray = list(self.history)
        # minVal = min(tmpArray)
        # tmpArray.sort()
        mean = sum(tmpArray) / len(tmpArray)
        self.buyingValueCoef = (tmpArray[-1]-mean)/mean
    
    def checkIfTheBiggest(self):
        tmpArray = list(self.history)
        # maxVal = max(tmpArray)
        # tmpArray.sort()
        mean = sum(tmpArray) / len(tmpArray)
        self.sellingValueCoef = (tmpArray[-1]-mean)/mean
    
if __name__ == "__main__":
    
    #initialisation
    sysInitFlag = False
    rawInput = input().split()
    moneyLeft = float(rawInput[0])
    stockNumber = int(rawInput[1])
    daysLeft = int(rawInput[2])
    
    stocks = []
    stocks = [Stock() for i in range(stockNumber)]
    treshold = 0.02
    
    while(daysLeft > 0):
        if sysInitFlag == True:
            rawInput = input().split()
            moneyLeft = float(rawInput[0])
            stockNumber = int(rawInput[1])
            daysLeft = int(rawInput[2])
        sysInitFlag = True
        
        # read data about the market
        for i in range(stockNumber):
            tmp = input().split()
            name = tmp[0]
            number = int(tmp[1])
            history = [float(x) for x in tmp[2:]]
            stocks[i].stackUpdate(name, number, history)
            # print("{} {} {}".format(stocks[i].name,stocks[i].predictedIncome, stocks[i].buyingValueCoef))
        
        numberOfOperations = 0
        ans = ""
        
        for i in range(stockNumber):
            # print("{} {} {}".format(stocks[i].name,stocks[i].predictedIncome, stocks[i].buyingValueCoef))

            if stocks[i].buyingValueCoef < -treshold and int(moneyLeft / stocks[i].history[-1]) > 0:
                numberOfOperations += 1
                ans += stocks[i].name
                ans += " BUY"
                ans += " "
                ans += str(int(moneyLeft / stocks[i].history[-1]))
                ans += '\n'
                moneyLeft = moneyLeft - stocks[i].history[-1]*int(moneyLeft / stocks[i].history[-1])
            if stocks[i].buyingValueCoef > treshold and stocks[i].number > 0:
                numberOfOperations += 1
                ans += stocks[i].name
                ans += " SELL"
                ans += " "
                ans += str(stocks[i].number)

        print(numberOfOperations)
        print(ans)
        