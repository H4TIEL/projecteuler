#include <iostream>
#include <cmath>
typedef unsigned long long int ulli;

// generate traingular number
ulli triangularNumber(ulli position, ulli accumulator) {
	if(position == 1) return accumulator;
	return triangularNumber(position - 1, position + accumulator);
}

// count divisors
int divisors(ulli number) {
	// upto
	double root = sqrt(number);
	int count = 0;
	for(int i = 1; i <= (int) root; i++) {
		if(number % i == 0) count = count + 2;
	}
	return count;
}

int main() {

	int factors = 1;
	ulli position = 1;
	while(factors < 500) {
		ulli num = triangularNumber(position, 1);
		factors = divisors(num);
		std::cout<<num;
       		std::cout<<": ";
		std::cout<<factors<<std::endl;
		position++;
	}
	return 0;
}

// 76576500
