# input :   [1, 2, 3, 4, 5]
# output :  [
#           (2 * 3 * 4 * 5),
#           (1 * 3 * 4 * 5),
#           (1 * 2 * 4 * 5),
#           (1 * 2 * 3 * 5),
#           (1 * 2 * 3 * 4)
#           ]

def mul_no_index(list):
    before = []
    after = []
    print ("my list", list)
    for item in list:
        if (before):
            before.append(before[-1] * item)
        else:
            before.append(item)
    print ("before array", before)

    for i in range(len(list), 0, -1):
        if (after):
            after.append(after[-1] * list[i - 1])
        else:
            after.append(list[i - 1])
    after = after[::-1]
    print ("after array", after)

    fin = []
    for i in range(len(list)):
        if (i == 0):
            fin.append(after[i + 1])
        elif (i == max(range(len(list)))):
            fin.append(before[i - 1])
        else:
            fin.append(before[i - 1] * after[i + 1])
    print (fin)
    return (fin)

def main():
    my_list = [1,2,3,4,5]
    mul_no_index(my_list)

if (__name__ == "__main__"):
    main()
