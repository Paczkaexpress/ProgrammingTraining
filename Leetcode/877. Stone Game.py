class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        Alex = 0
        size = len(piles)
        low = 0
        high = size
        for i in range(size):
            if i % 2 == 0:
                # print(sum(piles[low:high-size-1:2]))
                # print(sum(piles[high-size-1:low:-2]))
                if(sum(piles[low:high-size-1:2]) > sum(piles[high-size-1:low:-2])):
                    Alex += piles[low]
                    low += 1
                else:
                    Alex += piles[high-1]
                    high -= 1
                # print("Alex score {}".format(Alex))
            else:
                if(piles[low] > piles[high-1]):
                    Alex -= piles[low]
                    low += 1
                else:
                    Alex -= piles[high-1]
                    high -= 1
                # print("Lee score {}".format(Lee))
        
        # print(sum(piles[0::2]))
        # print(sum(piles[high::-2]))
        # print(Alex)
        # print(Lee)
        if(Alex > 0):
            return True
        else:
            return False