#include <iostream>
#include <cmath>

using namespace std;


bool isPerfectSquare(int square) {

	double squareroot = sqrt(square);
	
	double product = squareroot * squareroot;

	if(product == square) {
		return true;
	}

	return false;

}



int main() {

	int a = 2;
	int b = 3;
	int c = 0;
	int cSquare = a*2 + b*2;

	if(isPerfectSquare(cSquare)) {
		c = sqrt(cSquare);	
	}

	if(c != 0) {
		int sum = a + b + c;
		cout<<"c: "<<c<<endl;
		cout<<"Sum: "<<sum<<endl;
	}
	return 0;
}
