import math

class SegmentTree():
    def __init__(self, arr):
        self.arr = arr

        # cannot do this because some nodes are empty
        # st = [None] * (2 * len(arr) - 1)

        nlevel = math.ceil(math.log(len(arr), 2))

        nleave = math.pow(2, nlevel)
        nnodes = int(nleave * 2 - 1)
        st = [None] * nnodes
        self.constructHelper(0, len(arr) - 1, st, 0)

        self.st = st

    # arr: input array
    # ss: index of input array
    # si: current index in segment tree
    def constructHelper(self, ss, se, st, si):
        i = ss
        j = se

        # If there is one element in array, store it in current node of
        # segment tree and return
        if ss == se:
            st[si] = self.arr[ss]
            return st[si]

        m = (ss + se) // 2
        st[si] = self.constructHelper(ss, m, st, si * 2 + 1) + self.constructHelper(m + 1, se, st, si * 2 + 2)
        return st[si]

    # st: input array
    # ss, se: range represented by current node (inclusive)
    # qs, qe: range of query (inclusive)
    # si: index of current node (zero based)
    def getSumHelper(self, ss, se, qs, qe, si):
        # case 1: completely within, return ndoe val
        if qs <= ss and qe >= se:
            return self.st[si]

        # case 2: completely outside, return 0
        if se < qs or ss > qe:
            return 0

        # case 3: partial overlap, recurse
        m = (ss + se) // 2
        return self.getSumHelper(ss, m, qs, qe, 2 * si + 1) + self.getSumHelper(m + 1, se, qs, qe, 2 * si + 2)

    def getSum(self, qs, qe):
        if qs < 0 or qe > len(self.arr) - 1 or qs > qe:
            return -1

        return self.getSumHelper(0, len(self.arr) - 1, qs, qe, 0)

    # start with root, add diff to all nodes which have given index in their range
    # i: index of node to be updated
    # val: new_val - old_val
    def updateVal(self, i, val):
        if i < 0 or i > len(self.arr) - 1:
            return

        diff = val - self.arr[i]
        self.arr[i] = val

        self.updateValHelper(0, len(self.arr) - 1, i, diff, 0)

    def updateValHelper(self, ss, se, i, diff, si):
        if i < ss or i > se:
            return

        self.st[si] += diff
        if se != ss:
            m = (ss + se) // 2
            self.updateValHelper(ss, m, i, diff, 2 * si + 1)
            self.updateValHelper(m + 1, se, i, diff, 2 * si + 2)

arr = [1, 3, 5, 7, 9, 11]
st = SegmentTree(arr)
print(st.st)

print(st.getSum(0, 4))

st.updateVal(2, 10)
print(st.st)