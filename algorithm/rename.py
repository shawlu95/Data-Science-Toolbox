fname = "581. Shortest Unsorted Continuous Subarray"
print(fname.replace(".ipynb", "").replace(".", "").replace(" ", "_"))

l = [0, 1, 2, 3]
print(l[~0], l[~1], l[~2])
print(l[-0], l[-1], l[-2])
print(l[-1], l[-2], l[-3])


print("a  b       c".split())

# error
# print("a  b       c".split(""))

print("a  b       c".split(" "))


print([1, 2, 3, 4][:-2])

l = ["A", "B", "C"]
for i, item_1 in enumerate(l[:-2]):
    for j, item_2 in enumerate(l[i + 1:- 1]):
        for item_3 in l[j + 1:]:
            print(i, j, item_1, item_2, item_3)
            print("")

(user_1, user_2), count = ((1, 2), 3)
print(user_1, user_2, count)

triple = ("A", "B", "C")
print(list((triple + tuple(item) for item in triple[::-1])))

triple = ["A", "B", "C"]
print([tuple(triple[:idx] + triple[idx + 1:]) for idx in range(len(triple) - 1, -1, -1)])
print([tuple(triple[:idx] + triple[idx + 1:]) for idx in range(len(triple))][::-1])