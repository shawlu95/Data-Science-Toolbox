class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        common = None
        for a in A:
            count = {}
            for c in a:
                count[c] = count.get(c, 0) + 1
            
            # cannot use "not common" because empty dictionary is trusy
            # if common gets emptied, the result should be empty, not restarted
            if common is None:
                common = count
            else:
                # need to convert to key, or dictionary resizing throws error
                keys = list(common.keys())
                for key in keys:
                    if key in count:
                        common[key] = min(common[key], count[key])
                    else:
                        del common[key]
        ans = []
        print(common)
        for key, val in common.items():
            ans += [key for _ in range(val)]
        return ans
                        
                    
            
            
        
        
        