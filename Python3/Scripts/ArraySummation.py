from time import time

class Solver:
    def __init__(self, Arr:list) -> None:
        self.Arr:list = Arr
        if (self.Arr[0] > self.Arr[1]):
            self.minNumber:int = self.Arr[1]
            self.maxNumber:int = self.Arr[0]
        else: 
            self.minNumber:int = self.Arr[0]
            self.maxNumber:int = self.Arr[1]
        self.numLen:int = (self.maxNumber - self.minNumber)+1
    def getSum(self) -> int:
        self.maxPlusMin:int = (self.maxNumber+self.minNumber)
        add:int = int((self.maxPlusMin*self.numLen)/2)
        return add

def main() -> None:
    Arr:list = list()
    print ("Enter the elements Values: ")
    for _ in range(0,2): Arr.append(int(input()))
    startTime:float = time()
    solver:Solver = Solver(Arr)
    sum:int = solver.getSum()
    endTime:float = time()
    print ("the Sum is: {}".format(sum))
    print ("time taken: {} nanoSeconds".format((endTime-startTime)*1000000000))

if __name__ == "__main__":
    main()