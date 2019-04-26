# An efficient Python3 program
# to randomly select k items
# from a stream of items
import random


# A utility function
# to print an array
def printArray(stream, n):
    for i in range(n):
        print(stream[i], end=" ");
    print();


# A function to randomly select
# k items from stream[0..n-1].
def selectKItems(stream, n, k):
    i = 0;
    # index for elements
    # in stream[]

    # reservoir[] is the output
    # array. Initialize it with
    # first k elements from stream[]
    reservoir = [0] * k;
    for i in range(k):
        reservoir[i] = stream[i];

    # Iterate from the (k+1)th
    # element to nth element
    for i in range(k, n):
        # Pick a random index
        # from 0 to i.
        j = random.randrange(i + 1);

        # If the randomly picked
        # index is smaller than k,
        # then replace the element
        # present at the index
        # with new element from stream
        # adopt new element with prob k / (i + 1)
        if j < k:
            # j is uniformly random, so each existing item is equally
            # likely to be replaced (1/k), probability that each
            # existign element is replaced with new one is 1/(i+1)
            # complement prob i / (i + 1)
            # probability of old element remains: (k / i) * (i / (i + 1)) = k / (i + 1)
            # which is equal to new element being adopted (proof complete)
            reservoir[j] = stream[i];
        i += 1;

    print("Following are k randomly selected items");
    printArray(reservoir, k);


# Driver Code

if __name__ == "__main__":
    stream = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12];
    n = len(stream);
    k = 5;
    selectKItems(stream, n, k);