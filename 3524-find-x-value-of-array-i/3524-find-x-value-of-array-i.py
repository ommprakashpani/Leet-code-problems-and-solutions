class Solution(object):
    def resultArray(self, nums, k):
        result = [0] * k
        current_counts = [0] * k
        
        for num in nums:
            next_counts = [0] * k
            rem = num % k
            
            # Start a new subarray at the current element
            next_counts[rem] += 1
            
            # Extend previous subarrays to include the current element
            for v in range(k):
                if current_counts[v] > 0:
                    next_counts[(v * rem) % k] += current_counts[v]
            
            # Accumulate counts into the global result
            for x in range(k):
                result[x] += next_counts[x]
                
            current_counts = next_counts
            
        return result
            