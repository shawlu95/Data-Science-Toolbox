class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        global_count = {}
        
        for cpdomain in cpdomains:
            count, domain = cpdomain.split(" ")
            count = int(count)
            domain = domain.split(".")
            
            for i, sub in enumerate(domain):
                fullSub = ".".join(domain[i:]) # mind the end index 
                global_count[fullSub] = global_count.get(fullSub, 0) + count
        
        return [str(val) + " " + key for key, val in global_count.items()]