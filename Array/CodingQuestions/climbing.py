

#https://www.hackerrank.com/challenges/counting-valleys/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup


'''
An avid hiker keeps meticulous records of their hikes. During the last hike that took exactly  steps, for every step it was noted if it was an uphill, , or a downhill,  step. Hikes always start and end at sea level, and each step up or down represents a  unit change in altitude. We define the following terms:

A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level and ending with a step down to sea level.
A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level and ending with a step up to sea level.
Given the sequence of up and down steps during a hike, find and print the number of valleys walked through


Sample Input 
8
UDDDUDUU

Sample Output
1

Explanation:
_/\      _
   \    /
    \/\/
'''
def countingValleys(steps, path):
    
    v = 0
    up = 0
    down = 0
    for i in path:
        if(i == 'U'):
            up += 1
        elif(i  == 'D'):
            down += 1
        if((up - down) == 0 and i == 'U'):
            v+=1
    return (v)
    
print(countingValleys(12, "DDUUDDUDUUUD"))
