#include <iostream>
#include <cmath>

double func(double x) {
    return tan(x) - x;
}

double bisection(double a, double b, double eps) {
    if (func(a) * func(b) > 0) {
        std::cout << "There's no solutions in [" << a << ", " << b << "]" << std::endl;
        return 0;
    }

    double c = a;
    while ((b - a) >= eps) {
        c = (a + b) / 2;

        if (func(c) == 0.0)
            break;
        else if (func(c) * func(a) < 0)
            b = c;
        else
            a = c;
    }
    return c;
}

int main() {
    double a = 1, b = 2; // segment
    double eps = 0.01;   // accuracy

    std::cout << "Solution: " << bisection(4.4, 4.6, 0.1) << " Accuracy: 0.1" << std::endl;
    std::cout << "Solution: " << bisection(3, 4, 0.01) << " Accuracy: 0.01" << std::endl;
    std::cout << "Solution: " << bisection(-1.25, 0.625, 0.001) << " Accuracy: 0.001" << std::endl;


    return 0;
}
