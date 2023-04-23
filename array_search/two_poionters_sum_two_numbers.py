
# improve this version ---> problem https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# fix
# improve time of algorithm, no passt tes because it
# dont use set

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for index, value in enumerate(numbers):
            if value + numbers[index + 1] == target:

                return [index + 1, index + 2]

            i = index + 1

            while i <= len(numbers) - 1 and value + numbers[i] <= target:
                print(index, i)

                if value + numbers[i] == target:
                    return [index + 1, i + 1]

                i = i + 1
