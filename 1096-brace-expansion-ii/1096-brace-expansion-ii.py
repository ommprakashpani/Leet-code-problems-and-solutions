class Solution(object):
    def braceExpansionII(self, expression):
        # Base case: if there are no braces, just split by commas or return the word
        if "{" not in expression:
            return sorted(list(set([expression])))
        
        # Find the first innermost/valid {...} block
        i = expression.find("}")
        j = expression.rfind("{", 0, i)
        
        # Extract parts: left of the brace, inside the brace, right of the brace
        left = expression[:j]
        right = expression[i + 1:]
        inner = expression[j + 1:i]
        
        # Split inner expression by comma (respecting no nested commas since it's the first closing brace)
        # Wait, a simple comma split works for innermost because there are no inner braces inside 'inner'
        choices = inner.split(",")
        
        # Generate new expressions by replacing {inner} with each choice
        expanded = set()
        for choice in choices:
            new_expr = left + choice + right
            expanded.update(self.braceExpansionII(new_expr))
            
        return sorted(list(expanded))