#include <iostream>
#include <cmath>

using namespace std;

double func(double x) {
    return tan(x) - x;
}

double fi(double x) {
    return x - func(x);
}

int main() {
    double x0 = 1;

    double eps = 1e-10;

    double x = x0;
    int iter = 0;
    while (fabs(func(x)) > eps) {
        x = fi(x);
        iter++;
    }

    cout << "Solution: " << x << endl;
    cout << "Number of iterations: " << iter << endl;

    return 0;
}
