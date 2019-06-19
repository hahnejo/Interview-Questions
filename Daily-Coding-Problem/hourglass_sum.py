def hourglassSum(arr):
    sum = []
    for i in range(len(arr) - 2):
        for j in range(len(arr) - 2):
            sum.append(arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] +
                       arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2])
    max = sum[0]
    for i in range(len(sum)):
        if arr[i] > max:
            max = arr[i]
    return max

def main():
    my_arr = [  [0,0,0,5],
                [6,1,6,6],
                [0,0,1,5] ]

    print(hourglassSum(my_arr))

if __name__ == '__main__':
    main()
