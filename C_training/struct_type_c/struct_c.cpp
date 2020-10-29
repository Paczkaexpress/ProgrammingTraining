#include<iostream>

typedef struct testStruct
{
    int value1;
    int value2;
}test_t;

int main(int argc, char* argv[])
{

    test_t test = {.value1 = 1, .value2 = 2};
    std::cout<<testStruct.value1<<std::endl;
    std::cout<<test.value1<<" "<<test.value2<<std::endl;
}

// #include <stdio.h>

// typedef struct testStruct
// {
//     int value1;
//     int value2;
// }test_t;

// typedef struct NewtestStruct
// {
//     struct NewtestStruct* str;
//     int value1;
//     int value2;
// }NewtestStruct_t;

// int main()
// {
//     test_t test = {.value1 = 1, .value2 = 2};
    
//     NewtestStruct_t test1 = {.str = NULL, .value1 = 1, .value2 = 2};
//     NewtestStruct_t test2 = {.str = &test1, .value1 = 3, .value2 = 4};

//     printf("%d %d\n",test.value1, test.value2);
//     printf("%d %d %d %d\n",test2.value1, test2.value2, test2.str->value1, test2.str->value2);
//     return 0;
// }
