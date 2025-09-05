# Optimal solution for this problem - Hashing Method
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output_indices = {}
        for index, number in enumerate(nums):
            difference = target - number
            if difference in output_indices:
                return [index, output_indices[difference]]
            output_indices[number] = index


# LOGIC of the program
"""

Input : nums [List], target = 9
Output : the index of numbers which add up to 9

A. Brute Force Method
   1. Target - 1st element = 2nd element desired
   2. Search 2nd element desired in list and if found then return

B. Use of a hashmap
    1. Make an empty dictionary
    2. Start iteration in the nums list
    3. Calculate the difference
    4. If the difference is in the dictionary then return index of difference
       and current number in list
    5. If difference is not in dictionary then insert the number from the list
       into the dictionary
"""
