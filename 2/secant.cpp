#include <iostream>
#include <cmath>

using namespace std;

double func(double x) {
    return tan(x) - x;
}

double secnat(double x0, double x1, double delta) {
    double xn_1 = x0;
    double xn = x1;

    int counter = 0;
    while (fabs(xn_1 - xn) > delta) {
        double next = xn - func(xn) * (xn - xn_1) / (func(xn) - func(xn_1));
        xn_1 = xn;
        xn = next;
        counter++;
    }
    return xn;
}


int main() {
    double x0 = 4.45;
    double x1 = 4.5;

    double eps = 1e-6;

    auto result = secnat(x0, x1, eps);
    cout << "Solution: " << result << endl;

    return 0;
}
