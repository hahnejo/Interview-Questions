# need to count when there is a downhill
# once that downhill come up to the sea level
# then there is one valley

def count_valleys(n, data):
    status = 0
    valley_count = 0
    for step in data:
        if step == 'U':
            status += 1
            if status == 0:
                valley_count += 1
        else:
            status -= 1
        print status
    return valley_count

def main():
    n = 6
    data = "DDDUUU"
    print(count_valleys(n, data))

if __name__ == "__main__":
    main()