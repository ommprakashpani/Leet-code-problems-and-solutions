class SegmentTree:
    def __init__(self, nums, k):
        self.n = len(nums)
        self.k = k
        # Each node stores: (total_product % k, list_of_remainder_frequencies)
        self.tree = [None] * (4 * self.n)
        self.build(nums, 0, 0, self.n - 1)

    def build(self, nums, node, start, end):
        if start == end:
            val = nums[start] % self.k
            counts = [0] * self.k
            counts[val] = 1
            self.tree[node] = (val, counts)
            return

        mid = (start + end) // 2
        self.build(nums, 2 * node + 1, start, mid)
        self.build(nums, 2 * node + 2, mid + 1, end)
        self.tree[node] = self.merge(self.tree[2 * node + 1], self.tree[2 * node + 2])

    def merge(self, left, right):
        left_prod, left_counts = left
        right_prod, right_counts = right
        
        # Combined total product of the segment
        total_prod = (left_prod * right_prod) % self.k
        
        # Merge prefix remainder distributions
        merged_counts = list(left_counts)
        for rem, count in enumerate(right_counts):
            if count > 0:
                new_rem = (rem * left_prod) % self.k
                merged_counts[new_rem] += count
                
        return (total_prod, merged_counts)

    def update(self, node, start, end, idx, val):
        if start == end:
            v = val % self.k
            counts = [0] * self.k
            counts[v] = 1
            self.tree[node] = (v, counts)
            return

        mid = (start + end) // 2
        if start <= idx <= mid:
            self.update(2 * node + 1, start, mid, idx, val)
        else:
            self.update(2 * node + 2, mid + 1, end, idx, val)
        self.tree[node] = self.merge(self.tree[2 * node + 1], self.tree[2 * node + 2])

    def get_x_count(self, node, start, end, l, r, target_x, current_prod):
        # Out of bounds
        if start > r or end < l:
            return 0, current_prod
            
        # Segment lies fully within the queried range
        if l <= start and end <= r:
            prod, counts = self.tree[node]
            ans = 0
            for rem, count in enumerate(counts):
                if count > 0 and (rem * current_prod) % self.k == target_x:
                    ans += count
            return ans, (current_prod * prod) % self.k
            
        mid = (start + end) // 2
        ans_left, current_prod = self.get_x_count(2 * node + 1, start, mid, l, r, target_x, current_prod)
        ans_right, current_prod = self.get_x_count(2 * node + 2, mid + 1, end, l, r, target_x, current_prod)
        return ans_left + ans_right, current_prod


class Solution(object):
    def resultArray(self, nums, k, queries):
        """
        :type nums: List[int]
        :type k: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        n = len(nums)
        st = SegmentTree(nums, k)
        result = []
        
        for idx, val, start, x in queries:
            # 1. Update the value persistently
            st.update(0, 0, n - 1, idx, val)
            
            # 2. Find the count of matching valid suffix-removals in range [start, n-1]
            # We initialize current_prod to 1 because the baseline prefix multiplier is 1.
            ans, _ = st.get_x_count(0, 0, n - 1, start, n - 1, x, 1)
            result.append(ans)
            
        return result
