import collections


def read_a_line(txt):
    txt_array = txt.split()
    return int(txt_array[0]), int(txt_array[1])


def chop_array(array):
    result = []
    total_num = int(array[0])
    current_result = []
    for i in range(1, len(array)):
        # handle one test case per iteration
        if array[i] in "\n" and i < len(array):
            # parse one line
            line_to_read, dependencies = read_a_line(array[i + 1])
            current_result.append(line_to_read)
            current_result.append(dependencies)

            for line_to_add in range(i + 2, i + dependencies + 2, 1):
                current_result.append(array[line_to_add])
            result.append(current_result)
            current_result = []

    for i in range(len(result)):
        if i + 1 == 18:
            print(result[i][0], result[i][2:])

        num_hours = topological_sort(result[i][0], result[i][2:])
        print("Case #%i: %i" % (i + 1, num_hours))
        print(result[i][0], result[i][2:])
        buffer.append("Case #%i: %i\n" % (i + 1, num_hours))


def topological_sort(n, pairs):
    # convert to graph
    graph, indegree = helper(n, pairs)

    que = []
    for i in range(1, n+1):
        if indegree[i] == 0:
            que.append(i)

    # traverse graph
    hours = 0
    while que:
        size = len(que)
        hours += 1
        for _ in range(size):
            cur = que.pop(0)
            for nbr in graph[cur]:
                indegree[nbr] -= 1
                if indegree[nbr] == 0:
                    que.append(nbr)
    return hours


# build graph
def helper(n, pairs):
    graph = collections.defaultdict(list)
    indegree = collections.defaultdict(int)
    for p in pairs:
        t = p.strip().split()
        graph[int(t[0])].append(int(t[1]))
        indegree[int(t[1])] += 1
    return graph, indegree


buffer = []
file = open('task2-test-input.txt', 'r')
array = []
for line in file:
    array.append(line)
chop_array(array)

with open('task2_test_data.output.txt', 'w') as file:
    # takes approx. 10 minutes
    for line in buffer:
        file.write(line)