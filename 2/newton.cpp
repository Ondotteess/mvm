#include <iostream>
#include <cmath>

using namespace std;

double func(double x) {
    return tan(x) - x;
}

double der(double x) {
    return pow(1 / cos(x), 2) - 1;
}

double newton(double init, double eps, int minters) {
    double x = init;
    int iters = 0;

    while (fabs(func(x)) > eps && iters < minters) {
        x = x - func(x) / der(x);
        iters++;
    }

    return x;
}

int main() {
    double init = 1.0;
    double eps = 1e-6;
    int iters= 1000;


    cout << "Solution: " << newton(init, eps, iters) << endl;

    return 0;
}
