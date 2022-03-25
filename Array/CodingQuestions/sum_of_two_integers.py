'''
2. Determine if the sum of two integers is equal to the given value
Given an array of integers and a value, determine if there are any two integers
in the array whose sum is equal to the given value.
Return true if the sum exists and return false if it does not.
Consider this array and the target sums:
'''

'''

Runtime Complexity: Linear, O(n2)

Memory Complexity: Linear, O(1)
'''
def solution(inputNumbers, value):
    
    for i in inputNumbers:
        
        for j in inputNumbers:
            if i + j == value:
                return 1
                
    return 0
    

numbers = [2,1,7,7,6]
value = 5
print(solution(numbers, value))


'''

Runtime Complexity: Linear, O(n)

Memory Complexity: Linear, O(n)
'''

def find_sum_of_two(A, val):
  found_values = set()
  for a in A:
    if val - a in found_values:
      return True

    found_values.add(a)
    
  return False