# TASK 2
#
# Given an index limit, find all corresponding Fibonacci values up to that limit in a sequence
# and return the sum of all even Fibonacci numbers. See more details in the task description in
# your assessment paper.

fn = (0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,4181,6765)

def even_fibonacci_sum(limit):
    limit = 0

    for n in fn(range(1-10)):
        return n if / 2

print(even_fibonacci_sum(limit=10))






##### TESTS ####

# print(even_fibonacci_sum(limit=10))  # should be 44
# print(even_fibonacci_sum(limit=15))  # should be 188
# print(even_fibonacci_sum(limit=1))   # should be 0

#
# def two_largest_numbers(numbers):
#     for i in range(len(numbers)):
#         for j in range(len(numbers) - 1):
#             if numbers[j] > numbers[j + 1]:
#                 numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
#     return numbers[2]
#
#
# two_largest_numbers([400, 100, -1, 46, 3])