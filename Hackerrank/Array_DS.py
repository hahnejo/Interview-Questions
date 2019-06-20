def reverseArray(a):
    new = []
    for item in reversed(a):
        new.append(item)
    print (new)
    return new

def main():
    arr = [5,6,7,8]
    reverseArray(arr)

if __name__ == "__main__":
    main()