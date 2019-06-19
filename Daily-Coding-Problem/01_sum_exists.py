# take list and a k (number that adds up to)
# k subtracting from current number in the list
# if the answer is what we have in a new list
# then sum exists and return true

# a function that makes an array having set's property

# def return_set(list):
#     my_set = []
#     for item in list:
#         if (type(item) != 'int')
#             return False
#         list.append(item)

def is_integer(list):
    for item in list:
        if (isinstance(item, int) == False):
            print ("There is a non-integer value")
            return False
    print ("All is integer value")
    return True

def add_to_k(list, k):
    new_list = set()
    for item in list:
        if (k - item in new_list):
            return True
        new_list.add(item)
    print(new_list)
    return False

def main():
    my_list = [10, 2, 13]
    my_num = 22
    if (is_integer(my_list) == True):
        print(add_to_k(my_list, my_num))
        
if (__name__ == "__main__"):
    main()