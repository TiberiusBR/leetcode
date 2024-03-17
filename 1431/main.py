"""
There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.

Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.

Note that multiple kids can have the greatest number of candies.
"""


def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
    true_max = max(candies) - extraCandies
    return [candy >= true_max for candy in candies]


# runtime 37
# We define a fixed max value by subtracting the highest candy amount in the group by the extra candy.
# Then we iterate the list and check if the current kid has more or equal to our max candy amount.
# In this way, there will be no need to keep calling the max function, making our algorithm keep a time complexity of O(n)