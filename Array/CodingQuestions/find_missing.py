
'''
1. Faadfdaadaind the missing number in the array

You are given an array of positive numbers from 1 to n,
such that all numbers from 1 to n are present except one number x.
You have to find x. The input array is not sorted.
Look at the below array and give it a try before checking the solution.

'''
'''
Runtime Complexity: Linear, O(n)

Memory Complexity: Constant, O(1)
'''

##BRUTE FORCE

def find_missing(input):
    input.sort()
    numnLen = len(input)

    for i in range(numnLen+1):

        if (i == numnLen and i not in input ):
                return numnLen

        if(input[i] != i):
            return i



