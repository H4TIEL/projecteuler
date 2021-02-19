#include <iostream>
#include <chrono>
#include <cmath>

using namespace std::chrono;

int main() {
    auto start = high_resolution_clock::now();

    int p[8] = {2, 3, 5, 7, 11, 13, 17, 19};
    int n = 50;
    double multiple = 1;
    for (int i = 0; p[i] <= n; i++) {
        multiple *= pow(p[i], floor(log(n) / log(p[i])));
    }

    auto stop = high_resolution_clock::now();
    auto microDuration = duration_cast<microseconds>(stop - start);
    auto milliDuration = duration_cast<milliseconds>(stop - start);

    std::cout.precision(17);
    std::cout << "Multiple: " << multiple << std::endl;
    std::cout << "Time: " << microDuration.count() << "μs" << std::endl;
    std::cout << "Time: " << milliDuration.count() << "ms" << std::endl;
    return 0;
}