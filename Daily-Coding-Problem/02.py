# def multiply_wo_i(list):
#     left_elem = []
#     right_elem = []
#     new_list = [None] * len(list)

#     for item in list:
#         if (left_elem):
#             left_elem.append(left_elem[-1] * item)
#         else:
#             left_elem.append(item)
#     print(left_elem)

#     for item in reversed(list):
#         if (right_elem):
#             right_elem.append(right_elem[-1] * item)
#         else:
#             right_elem.append(item)
#     print(right_elem)
    
    # right_elem = list(reversed(right_elem))

    # result = []
    # for i in range(len(list)):
    #     if i == 0:

def products(nums):
    # Generate prefix products
    prefix_products = []
    for num in nums:
        if prefix_products:
            prefix_products.append(prefix_products[-1] * num)
        else:
            prefix_products.append(num)
    print(prefix_products)
    # Generate suffix products
    suffix_products = []
    for num in reversed(nums):
        if suffix_products:
            suffix_products.append(suffix_products[-1] * num)
        else: 
            suffix_products.append(num)
    suffix_products = list(reversed(suffix_products))

    # Generate result
    result = []
    for i in range(len(nums)):
        if i == 0:
            result.append(suffix_products[i + 1])
        elif i == len(nums) - 1:
            result.append(prefix_products[i - 1])
        else:
            result.append(prefix_products[i - 1] * suffix_products[i + 1])
    print(result)
    return result


def main():
    my_list = [1, 2, 3, 4, 5]
    products(my_list)

if (__name__ == "__main__"):
    main()