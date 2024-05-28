class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i + 1 == len(flowerbed) or flowerbed[i + 1] == 0):
                n -= 1
                flowerbed[i] = 1
        return True if n <= 0 else False