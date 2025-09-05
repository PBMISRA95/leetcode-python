"""
Solved on - 01st May 2025
Author - Priyabrat Mishra
"""


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        i = 0
        while i < len(word1) or i < len(
            word2
        ):  # Until the characters of both the words are exhausted
            if i < len(word1):
                merged.append(word1[i])  # if chars left in 1st word append it to merged: List
            if i < len(word2):
                merged.append(word2[i])  # if chars left in 2nd word append it to merged: List
            i += 1
        return "".join(merged)  # Merge is a list converted to string and returned
