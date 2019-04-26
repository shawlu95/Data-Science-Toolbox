import collections
import string
def findLadders(start, end, dic):
    dic.add(end)
    level = {start}

    # maps permutation to its parent, each parent can have multiple children
    parents = collections.defaultdict(set)
    while level and end not in parents:
        next_level = collections.defaultdict(set)
        for node in level:
            for char in string.ascii_lowercase:
                for i in range(len(start)):
                    n = node[:i]+char+node[i+1:]
                    if n in dic and n not in parents:
                        next_level[n].add(node)
        level = next_level
        parents.update(next_level)
    res = [[end]]
    while res and res[0][0] != start:
        res = [[p]+r for r in res for p in parents[r[0]]]
    return res

print(findLadders("hit",  "cog", {"hot","dot","dog","lot","log","cog"}))