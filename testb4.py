

#     count = 0
#     for n in nums:
#         # if n.iseven():
#         count += 1
#         count = count + 1
#     return count
#     # if nums == [2, 4]:
#     #     return True
#     # return False
# # def foo(banana):
#     assert foo([]) == 0, "No numbers"
#     assert foo([1, 6]) == 2, "Two numbers"
# def even_number_of_evens(nums):
#     if nums == [2, 4]:
#         return True
#     return False
# -------------------------------------------------------------
# def number_of_evens(nums):
#     number_of_evens = sum([1 for n in nums is n 2% == 0])

#     if number_of_evens == 0:
#         return False
    
#     if number_of_evens 2% == 0:
#         return True
#     else:
#         return False
    
# def even_number_of_evens(nums):
#     evens = 0
    
#     for num in nums:
#         if num%2 == 0:
#             evens += 1
            
#     if evens == 0:
#         return False
#     return evens%2 == 0

    
        
        
assert even_number_of_evens([]) == False, "No numbers"
assert even_number_of_evens([2]) == False, "One even number"
assert even_number_of_evens([2, 4]) == True, "Two even numbers"
assert even_number_of_evens([2, 3]) == False, "Two numbers, only one even"
assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8]) == False, "Multiple numbers, three are even"
assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8, 5, 12]) == True, "Multiple numbers, four are even"
assert even_number_of_evens([1, 3, 9]) == False, "No even numbers"

print("All Tests Pass!")