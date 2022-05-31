TASK 3

Validate subsequence. Use suggested tests below to check
correctness of your solution.




#### TESTS ####

array1 = [5,1,22,25,6,-1,8,10]
sequence1 = [1,6,-1,-2]

print(is_valid_subsequence(array1, sequence1))  # FALSE

array2 = [5,1,22,25,6,-1,8,10]
sequence2 = [1,6,-1, 10]

print(is_valid_subsequence(array2, sequence2))  # TRUE

array3 = [5,1,22,25,6,-1,8,10]
sequence3 = [25]

print(is_valid_subsequence(array3, sequence3))  # TRUE
