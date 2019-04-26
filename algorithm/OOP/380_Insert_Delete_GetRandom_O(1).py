import random


class RandomizedSet(object):

    def __init__(self):
        self.nums = []
        self.pos = {}

    def insert(self, val):
        if val in self.pos:
            return False

        self.nums.append(val)

        # pos maps value to idx
        self.pos[val] = len(self.nums) - 1
        return True

    def remove(self, val):
        if val not in self.pos:
            return False

        # get index of value to be removed
        idx, last = self.pos[val], self.nums[-1]

        # removed position is filled with last element
        self.nums[idx], self.pos[last] = last, idx

        # remove last element
        self.nums.pop()

        # remove key of removed element
        del self.pos[val]

        return True

    def getRandom(self):
        return self.nums[random.randint(0, len(self.nums) - 1)]

