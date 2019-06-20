def hourglassSum(arr):
    collection = []
    for i in range(len(arr) - 2):
        for j in range(len(arr) - 2):
            collection.append(arr[i][j]+arr[i][j+1]+arr[i][j+2]+
                              arr[i+1][j+1]+
                              arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2])
    big = collection[0]
    for item in collection:
        if item > big:
            big = item
    return big
        
def main():
    arr = [[1,1,1,1,1],
           [2,2,2,2,2],
           [2,2,6,2,2],
           [2,2,2,2,2],
           [2,2,2,2,2]]

    hourglassSum(arr)

if __name__ == "__main__":
    main()