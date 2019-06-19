// Find the sum of all multiples of 3 or 5 below 1000.

// 1. get multiple of 3.
//      return the list that has multiples of 3 less than 1000
// 2. get multiple of 5.
//      return the list that has multiples of 5 less than 1000
// 3. find overlapping number.
//      takes in two lists and compares them to get same number.
// 4. add all those listed numbers.
// 5. create a new list combining those two.

 #include <stdio.h>
#include <stdlib.h>

 int     *multiple_3(void)
{
    int i;
    int ans;
    int *arr;
    int count;

     i = 0;
    count = 1;
    ans = 3;
    arr = malloc(sizeof(int) * 1000);
    while (ans >= 3 && ans <= 1000)
    {
        ans = 3 * count;
        if (ans % 3 == 0)
            arr[i] = ans;
        printf("arr[%d] = %d\n", i, arr[i]);
        count++;
        i++;
    }
    return (arr);
    free (arr);
}

 int     *multiple_5(void)
{
    int i;
    int ans;
    int *arr;
    int count;

     i = 0;
    count = 1;
    ans = 5;
    arr = malloc(sizeof(int) * 1000);
    while (ans >= 5 && ans <= 1000)
    {
        ans = 5 * count;
        if (ans % 5 == 0)
            arr[i] = ans;
        printf("arr[%d] = %d\n", i, arr[i]);
        count++;
        i++;
    }
    return (arr);
    free (arr);
}

//  void    take_two_add_them(int *mul_3, int *mul_5)
// {
//     while (mul_3[i])
//     {

//      }
// }

 int main()
{
    multiple_3();
    multiple_5();
    return (0);
}