
# Se itiliza hashmap para almacenar los indices de los numeros
# y se busca el complemento necesario para alcanzar el objetivo.

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        prevMap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return []


print(Solution().twoSum([2, 7, 11, 15], 9))  # Example usage