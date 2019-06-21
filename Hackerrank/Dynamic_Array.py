# seqList contains seq
# "a list containing lists"

from itertools import repeat

arr = [[1,0,5],
       [1,1,7],
       [1,0,3],
       [2,1,0],
       [2,1,1]]
n = 2
queries = 5
seqList = [ [] for i in repeat(None, n) ]

def query_1(x, y):
    seqList.append(y)
    x ^ lastAns % n
    print ("x is ", x)
    print ("y is ", y)

def query_2(x, y):
    print ("x is ", x)
    print ("y is ", y)
    y % size

def dynamicArray(n, queries):
    # make n amounts of array
    # in this case make two arrays
    print (seqList)
    lastAns = 0
    for i in range(len(arr)):
        if i == 1:
            query_1(arr[i][1], arr[i][2])
        else:
            query_2(arr[i][1], arr[i][2])

def main():
    dynamicArray(n, queries)

if __name__ == "__main__":
    main()
