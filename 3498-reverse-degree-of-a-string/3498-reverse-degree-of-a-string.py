class Solution(object):
    def reverseDegree(self, s):
        total_sum = 0
    
        for i, char in enumerate(s):
            # 1-indexed position in the string
            string_index = i + 1
            
            # Position in the reversed alphabet ('a' = 26, 'b' = 25, ..., 'z' = 1)
            # ord('z') is 122. If char is 'a' (97), 122 - 97 + 1 = 26
            reversed_alphabet_val = ord('z') - ord(char.lower()) + 1
            
            # Add the product to the running total
            total_sum += reversed_alphabet_val * string_index
            
        return total_sum