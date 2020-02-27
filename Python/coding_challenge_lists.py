"""
Create a function called every_three_nums that has one parameter named start.
The function should return a list of every third number between start and 100 (inclusive).
For example, every_three_nums(91) should return the list [91, 94, 97, 100].
If start is greater than 100, the function should return an empty list.
"""

#Write your function here
def every_three_nums(start):
  if start <= 100:
    return([start, (start + 3), (start + 6), (start + 9)])
  else:
    return([])

#Uncomment the line below when your function is done
print(every_three_nums(91))
#Returns [91, 94, 97]



"""
Create a function named more_frequent_item that has three parameters named lst, item1, and item2.

Return either item1 or item2 depending on which item appears more often in lst.

If the two items appear the same number of times, return item1.
"""

#Write your function here
def more_frequent_item(lst, item1, item2):
  if (lst.count(item2)) > (lst.count(item1)):
    return item2
  else:
    return item1

#Uncomment the line below when your function is done
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))

#Uncomment the line below when your function is done
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))
#returns 3
