# Alhamdulillah solved by myself within 9 minutes
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        cleaned_s = [char for char in s if char.isalnum()]
        cleaned_s = ''.join(cleaned_s)
        return cleaned_s == cleaned_s[::-1]



s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))
print(s.isPalindrome("race a car"))
print(s.isPalindrome(" "))
