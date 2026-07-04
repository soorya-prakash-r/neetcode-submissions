class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        x = 0
        y = len(numbers) - 1
        temp = 0
        while x < y:
            temp = numbers[x] + numbers[y]
            if temp == target:
                return [x+1, y+1]
            if temp < target:
                x += 1
            else:
                y -= 1
