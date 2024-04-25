#include <iostream>
#include <cmath>

using namespace std;

double derivative(double initial) {
    return 1 / (cos(initial) * cos(initial)) - 1; 
}

double func(double x) {
    return tan(x) - x;
}

double fi(double x, double lamb) {
    return x - lamb * (tan(x) - x);
}

double gi(double x, double x1 = 0) {
    return x - func(x);
}

double iterations(double x0, double eps) {
    double lamb = 1 / derivative(x0); 

    double x1 = fi(x0, lamb);

    int counter = 0;
    while (fabs(x1 - fi(x1, lamb)) > eps) {
        x1 = fi(x1, lamb);
        counter++;
    }

    return x1;
}

int main() {
    double initial = -1;
    double eps = 0.00001;

    auto result = iterations(initial, eps);
    cout << "Solution: " << result << endl;

    return 0;
}
