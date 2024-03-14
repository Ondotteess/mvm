#include <iostream>


int main() {

    float epsilon_float = 1.0f;
    double epsilon_double = 1.0f;

    auto counter_float = 0;
    while ((epsilon_float / 2 + 1.0f) != 1.0f) {
        epsilon_float /= 2;
        counter_float += 1;
    }

    auto counter_double = 0;
    while ((epsilon_double / 2 + 1.0f) != 1.0f) {
        epsilon_double /= 2;
        counter_double += 1;
    }

    std::cout << "Pow for float: "  << counter_float  << std::endl;
    std::cout << "Pow for double: " << counter_double << std::endl;

    // |_ _..._ _..._|
    //  S   E     M
    //  1   8     23

    std::cout << (1 < 1 + epsilon_float) << std::endl;

    std::cout << (1 == 1 + epsilon_float / 2) << std::endl;

    std::cout << (1 + epsilon_float == 1 + epsilon_float / 2) << std::endl;

    std::cout << (1 + epsilon_float + epsilon_float / 2 == \
                  1 + epsilon_float / 2 + epsilon_float ) << std::endl;


    return 0;
}
