class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output_indices = []
        for index, number in enumerate(nums):
            first_index = index
            first_number = number
            desired_target = target - number
            print(f"First index is : {first_index} and first number is : {first_number}")
            for index, value in enumerate(nums[first_index + 1 :]):
                print(f"The remaning numbers are value {value} at index {index}")
                if desired_target < 0:
                    break
                else:
                    for index, number in enumerate(nums):
                        if first_number != number:
                            # if first_index != index:
                            if desired_target == number:
                                second_index = index
                                second_number = number
                                print(
                                    f"Second index is : {second_index} and second number is : {second_number}"
                                )

        # print(output_indexes)
        # print(f"The index is {index} and number is {number} and the desired target is {desired_target}")


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
