"""
LeetCode 217 — Contains Duplicate
https://leetcode.com/problems/contains-duplicate/

Approach: Iterate through the list, keeping track of numbers seen so far.
If a number is already in the seen list, return True. Otherwise, return False.

Time complexity:  O(n^2) — `in` on a list is O(n), done inside a loop of length n
Space complexity: O(n)  — the seen list can grow to size n
"""

class Solution:
    def containsDuplicate(self, nums):
        seen = []

        for number in nums:
            if number in seen:
                return True
            seen.append(number)
        return False