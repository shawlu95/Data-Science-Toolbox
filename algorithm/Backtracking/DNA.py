strands = ['CCCCTTTGAGAGA', 'AGATCTCTCTC', 'GGAAAATCCCC', 'CTCTATATATATA']

def back_track(list_of_strings, used):
    if len(used) == len(list_of_strings):
        print(result)
        print("hello")
        return
    for i in range(len(list_of_strings)):
        if i not in used:
            if result[-1][-3:] == list_of_strings[i][0:3]:
                result.append(list_of_strings[i])
                used.append(i)
                back_track(list_of_strings, used)
                result.pop()
                used.pop()

for i in range(len(strands)):
    result = [strands[i]]
    used = [i]
    back_track(strands, used)
# back_track(strands, used)