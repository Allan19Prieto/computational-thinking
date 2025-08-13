
# Se itiliza hashmap para almacenar los indices de los numeros
# y se busca el complemento necesario para alcanzar el objetivo.
# Si se encuentra el complemento, se devuelve la lista de indices.
# Este enfoque tiene una complejidad de tiempo O(n) y una complejidad de espacio O(n).
# Este es un ejemplo de la solución al problema "Two Sum" en LeetCode.
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