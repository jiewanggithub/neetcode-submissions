class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        counter1, counter2 = Counter(s1), Counter(s2[:len(s1)])
        matches = 0
        for i in range(26):
            ch = chr(ord("a") + i)
            if counter1[ch] == counter2[ch]:
                matches += 1
        
        left = 0
        for right in range(len(s1), len(s2)):
            if matches == 26:
                return True  

            counter2[s2[left]] -= 1
            if counter2[s2[left]] == counter1[s2[left]]:
                matches += 1
            elif counter2[s2[left]] + 1 == counter1[s2[left]]:
                matches -= 1

            counter2[s2[right]] += 1
            if counter2[s2[right]] == counter1[s2[right]]:
                matches += 1
            elif counter2[s2[right]] - 1 == counter1[s2[right]]:
                matches -= 1
            left += 1 

        return matches == 26

            

             


        