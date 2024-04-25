#include <iostream>
#include <cmath>
#include <vector>

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

        //std::cout << "[ " << a << ", " << b <<  "]\n\n";

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

    //segments
    std::vector<double> first = {-1.5, 1} ; 
    std::vector<double> second = { 4.4, 4.6 };
    std::vector<double> third = { 10.6, 10.99 };

    double eps = 0.0001;   

    std::cout << "Solution: " << bisection(first[0], first[1], eps) 
        << " Accuracy: " << eps << std::endl << std::endl;

    std::cout << "Solution: " << bisection(second[0], second[1], eps) 
        << " Accuracy: " << eps << std::endl << std::endl;

    std::cout << "Solution: " << bisection(third[0], third[1], eps) 
        << " Accuracy: " << eps << std::endl << std::endl;


    return 0;
}
