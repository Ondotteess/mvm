#include <iostream>
#include <cmath>

using namespace std;

double equationFunction(double x) {
    return tan(x) - x;
}

double derivativeFunction(double x) {
    return pow(1 / cos(x), 2) - 1;
}

double newtonMethod(double initialGuess, double epsilon, int maxIterations) {
    double x = initialGuess;
    int iterations = 0;

    while (fabs(equationFunction(x)) > epsilon && iterations < maxIterations) {
        x = x - equationFunction(x) / derivativeFunction(x);
        iterations++;
    }

    return x;
}

int main() {
    double initialGuess = 1.0; 
    double epsilon = 1e-6;
    int maxIterations = 1000; 

    double solution = newtonMethod(initialGuess, epsilon, maxIterations);

    cout << "Solution: " << solution << endl;

    return 0;
}
