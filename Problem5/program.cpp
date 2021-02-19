#include <iostream>
#include <chrono>

using namespace std::chrono;

int main() {
    auto start = high_resolution_clock::now();
    bool isMultiple = false;
    int n = 20;
    int multiple = 2520;

    while (!isMultiple) {
        for (int i = 2; i <= n; i++) {
            if (multiple % i == 0) {
                if (i == n) {
                    isMultiple = true;
                    std::cout << "Multiple: " << multiple << std::endl;
                }
                continue;
            } else {
                multiple += 2520;
                break;
            }
        }

    }
    auto stop = high_resolution_clock::now();
    auto microDuration = duration_cast<microseconds>(stop - start);
    auto milliDuration = duration_cast<milliseconds>(stop - start);

    std::cout << "Time: " << microDuration.count() << "μs" << std::endl;
    std::cout << "Time: " << milliDuration.count() << "ms" << std::endl;
    return 0;
}
