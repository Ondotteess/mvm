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

    std::cout << epsilon_float << std::endl;
    std::cout << epsilon_double << std::endl;

    //bias = 2^(w-1) - 1 
    //xnorm = (-1)^s * (1+M/2^n) * 2^(E+1-2^(w-1))
    //xsubnorn = (-1)^s * (M/2^n)*2^(2-2^(w-1))

    std::cout << "W for float: " << 32 - counter_float - 1 << std::endl;
    //  Emax  =  2^2^7 - 1  =  2^(127) 
    //  Emin  = 2^(-149)  (subnorm)

    float a = 1;
    auto counter = 0;
    while (!std::isinf(a)) {
        a *= 2;
        counter++;
    }
    std::cout << "Emax for float: " << counter << std::endl;        // 2^128



    double b = 1;
    counter = 0;

    while (!std::isinf(b)) {
        b *= 2;
        counter++;
    }
    std::cout << "Emax for double: " << counter << std::endl;        // 2^1024


    float c = 1;
    counter = 0;
    while (c != 0) {
        c /= 2;
        counter++;
    }

    std::cout << "Emin for float: " << counter << std::endl;       //   2^150

    double d = 1;
    counter = 0;
    while (d != 0) {
        d /= 2;
        counter++;
    }

    std::cout << "Emin for double: " << counter << std::endl;      // 2^1075


    /*
        |_ _..._ _..._|
         S   E     M         float
         1   8     23

        |_ _..._ _..._|
         S   E     M         double
         1   11     52
     */

    std::cout << (1 < 1 + epsilon_float) << std::endl;
    std::cout << (1 == 1 + epsilon_float / 2) << std::endl;
    std::cout << (1 + epsilon_float > 1 + epsilon_float / 2) << std::endl;  // По определению eps

    std::cout << (1 + epsilon_float + epsilon_float / 2 >
        1 + epsilon_float / 2 + epsilon_float) << std::endl;    // Из-за неассоциативности



    std::cout << (1 + epsilon_float < 1 + epsilon_float + epsilon_float / 2)
        << std::endl;        // Округление


    return 0;
}
