"""
You have a long flowerbed in which some of the plots are planted, and some are not. 
However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n,
 return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.
"""


def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
    if n == 0:
        return True
    for idx, flower in enumerate(flowerbed):
        if n == 0:
            return True
        if idx == 0:
            if len(flowerbed) == 1 and flower == 0:
                return True
            if flowerbed[idx] == 0 and flowerbed[idx + 1] == 0:
                flowerbed[idx] += 1
                n -= 1
            continue
        if idx == len(flowerbed) - 1:
            if flowerbed[idx] == 0 and flowerbed[idx - 1] == 0:
                flowerbed[idx] += 1
                n -= 1
            continue
        if flowerbed[idx - 1] == 0 and flower == 0 and flowerbed[idx + 1] == 0:
            flowerbed[idx] += 1
            n -= 1
            continue
    return n == 0

#runtime 131 ms
#I believe it still can be optimized by removing some ifs.
#We start by checking if n == 0, which means there's no new flowers to plant, in this case, we can yes plant 0 new flowers.
#We iterate our flowerbed and check for our first and last indexes, and check if the index is empty (0) before or after.
#Then we check if the current index is surrounded by empty flowerbeds. If it is, then we plant a flower and diminish the current amount.