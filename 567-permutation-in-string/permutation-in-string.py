class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False

        # Frequency arrays for s1 and the first window of s2
        s1arr = [0] * 26
        s2arr = [0] * 26
        
        # Fill initial frequency arrays
        for i in range(len(s1)):
            s1arr[ord(s1[i]) - ord('a')] += 1
            s2arr[ord(s2[i]) - ord('a')] += 1

        # Check the first window before sliding
        if s1arr == s2arr:
            return True

        # Sliding window process
        for j in range(len(s1), len(s2)):
            s2arr[ord(s2[j]) - ord('a')] += 1  # Add new character to window
            s2arr[ord(s2[j - len(s1)]) - ord('a')] -= 1  # Remove old character

            if s1arr == s2arr:  # Check if permutation exists
                return True

        return False