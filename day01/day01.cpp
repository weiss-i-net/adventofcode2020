#include <iostream>
#include <vector>

int main() {
    int in_int;
    std::vector<int> int_vec;
    while (std::cin >> in_int)
        int_vec.push_back(in_int);
    for (int i = 0; i < int_vec.size(); ++i)
        for (int j = i + 1; j < int_vec.size(); ++j) {
            if (int_vec[i] + int_vec[j] == 2020)
                std::cout << "Part 1: " << int_vec[i] * int_vec[j] << '\n';
            for (int q = j + 1; q < int_vec.size(); ++q) {
                if (int_vec[i] + int_vec[j] + int_vec[q] == 2020)
                    std::cout << "Part 2: " << int_vec[i] * int_vec[j] * int_vec[q] << '\n';
            }
        }
    return -1;
}

