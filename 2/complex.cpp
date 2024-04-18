#include <iostream>
#include <complex>

using namespace std;

complex<double> polynomial(complex<double> z) {
    return pow(z, 3.0) - 1.0;
}

complex<double> derivative(complex<double> z) {
    return 3.0 * pow(z, 2.0);
}

complex<double> newtonMethod(complex<double> initialGuess, double epsilon, int maxIterations) {
    complex<double> z = initialGuess;
    int iterations = 0;

    while (abs(polynomial(z)) > epsilon && iterations < maxIterations) {
        z = z - polynomial(z) / derivative(z);
        iterations++;
    }

    return z;
}

int main() {
    double epsilon = 1e-6; 
    int maxIterations = 1000;

    complex<double> initialGuesses[3] = {complex<double>(1.0, 0.0), 
                                          complex<double>(-0.5, 0.5 * sqrt(3.0)), 
                                          complex<double>(-0.5, -0.5 * sqrt(3.0))};

    cout << "Solutions z^3 - 1:\n";
    for (int i = 0; i < 3; ++i) {
        complex<double> root = newtonMethod(initialGuesses[i], epsilon, maxIterations);
        cout << "Solution: " << i + 1 << ": " << root << endl;
    }

    return 0;
}
