class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = "aeiouAEIOU"
        s = list(s)   # convert to list for swapping
        i, j = 0, len(s) - 1
        
        while i < j:
            # move i forward until vowel found
            while i < j and s[i] not in vowels:
                i += 1
            # move j backward until vowel found
            while i < j and s[j] not in vowels:
                j -= 1
            # swap vowels
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        
        return "".join(s)
