#include <iostream>
#include <stdio.h>

using namespace std;

long long invertNumber(long long);

int main() 
{
	long long numOfTests = 0;
	long long number1 = 0;
	long long number2 = 0;
	long long number_inv1 = 0;
	long long number_inv2 = 0;
	long long sum_inv = 0;
		
	scanf("%d", &numOfTests);
    
    for(int i = 0;i<numOfTests; i++)
    {
    	long long number_inv1 = 0;
		long long number_inv2 = 0;
		long long sum_inv = 0;
	
    	scanf("%d %d", &number1, &number2);

		number_inv1 = invertNumber(number1);
		number_inv2 = invertNumber(number2);
		sum_inv = invertNumber(number_inv1 + number_inv2);
		
		printf("%d \n",sum_inv);

	}
    return 0;
}

long long invertNumber(long long number)
{
	long long inv_number = 0;
	while(number>0)
	{
		inv_number = 10 * inv_number;
		inv_number = inv_number + number%10;
		number = number / 10;
	}
	return inv_number;
}
