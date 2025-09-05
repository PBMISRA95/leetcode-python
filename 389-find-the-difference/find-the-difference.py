class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_sum = 0
        t_sum = 0

        s_sum = sum(ord(char) for char in s)
        t_sum = sum(ord(char) for char in t)

        return chr(t_sum - s_sum)

        """
        My INTITAL LOGIC
        for char in s:
            #print(f"char of s : {char} and corresponding ASCII value - {ord(char)} ")
            s_sum += (ord(char))
        #print(f"Sum of ASCII values of all characters of s is {s_sum}\n\n")

        for char in t:
            #print(f"char of t : {char} and corresponding ASCII value - {ord(char)} ")
            t_sum += (ord(char))
        #print(f"Sum of ASCII values of all characters of t is {t_sum}\n\n")

        #print(f"The missing letter is: {chr(t_sum-s_sum)}")
        return chr(t_sum-s_sum)
"""


"""
Problem statement -  2 input strings.
 t builds on top of s with extra character. Write which character is added.

Problem pattern -

 Logic -
 1.Brute Force - Sort both the strings. Then compare them character wise!
 2. Count the frequency of each character in each of the string and store it in a respective dictionaries. Them compare each of the
 dictionaries and whichever character is extra then that is the extra character added in t.
 3. Sum all the character values of t and s. Now subtract t - s = extra remaning character.


 """
