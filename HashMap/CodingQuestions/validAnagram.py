

#. 242. Valid Anagram

#Link: https://leetcode.com/problems/valid-anagram/

#Note: Use a hash-map to identify the ocurrency of each char

#Big O notation: Time O(n): Memory: O(n)

#######################################

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if(len(s) != len(t)):
            return False
        
        sWord ={}
        tWord = {}
        
        
        for i in range(len(s)):
            
            if(s[i] in sWord):
                sWord[s[i]] += 1
            else:
                sWord[s[i]] = 1
            
                      
            if(t[i] in tWord):
                tWord[t[i]] += 1
            else:
                tWord[t[i]] = 1
                
        
        for i in s:
            
            if(i in sWord and i in tWord):
                if(sWord[i] != tWord[i]):
                    return False
            else:
                return False
            
                      
      
        return True
