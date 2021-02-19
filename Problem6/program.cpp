#include <iostream>
#include <chrono>
#include <cmath>

using namespace std::chrono;

int main() {
    auto start = high_resolution_clock::now();

    int n = 100;

    // sum of natural numbers n (n + 1)  / 2
    int sumNatural = (n *(n + 1)) / 2;
    int squareOfsumNatural = pow(sumNatural, 2);

    // sum of squares n (n + 1) (2n + 1)  / 6
    int sumSquaresNatural = (n * (n + 1) * (2 * n + 1)) / 6;

    // Calculate differences
    int difference = squareOfsumNatural - sumSquaresNatural;

    std::cout << "Sum Squares of Natural: " << sumSquaresNatural << std::endl;
    std::cout << "Square of Sum of Natural: " << squareOfsumNatural << std::endl;
    std::cout << "Difference:  " << difference << std::endl;

    auto stop = high_resolution_clock::now();
    auto microDuration = duration_cast<microseconds>(stop - start);
    auto milliDuration = duration_cast<milliseconds>(stop - start);

    std::cout << "Time: " << microDuration.count() << " microseconds" << std::endl;
    std::cout << "Time: " << milliDuration.count() << " milliseconds" << std::endl;
    return 0;
}
