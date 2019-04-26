from math import floor, ceil

def roundNumbers(input):
    print('input:', input)

    # first round down all numbers, this will be lower than the target number. The difference is remember in the remain variable
    output = [floor(i) for i in input]
    remain = int(round(sum(input) - sum(output)))
    print('after floor:', output)
    print('remaining:', remain)

    # next round up some number, the # of numebrs to round up equal the remain
    # round up number with highest decimal values first
    it = sorted(enumerate(input), key=lambda i: ceil(i[1]) - i[1])
    print('sort_result:', it)

    # enumerate list, to remember index
    for i in range(0, remain):
        index = it[i][0]
        output[index] += 1
    print('final_output:', output)
    return output

roundNumbers([30.3, 2.4, 3.5])