class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        if len(arr) < 3:
            return False
        up = True
        down = False
        for i in range(1, len(arr)):
            if arr[i] == arr[i - 1]:
                return False
            elif arr[i] > arr[i - 1] and up:
                down = True
            elif arr[i] < arr[i - 1] and down:
                up = False
            else:
                return False
        if not up and down:
            return True
        return False