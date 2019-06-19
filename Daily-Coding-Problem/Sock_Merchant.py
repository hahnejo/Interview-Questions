# what is happening in sockMerchant function?
# first make a counter (tally) for each kind of sock
# second you will traverse ar (all socks again)
# count up in the talley when that particular kind is seen

def sockMerchant(n, ar):
    my_dict = set(ar)
    my_dict = {item: 0 for item in my_dict}
    for sock in ar:
        my_dict[sock] += 1
    for item in my_dict:
        my_dict[item] //= 2
    total = sum(my_dict.values())
    print total
    return total

def main():
    n = 9
    socks = [1,2,2,1,1,3,5,1,2]
    sockMerchant(n, socks)

if __name__ == '__main__':
    main()