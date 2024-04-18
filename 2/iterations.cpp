#include <iostream>
#include <cmath>

using namespace std;

double nextIteration(double x) {
    return atan(x); 
}

bool isConverged(double x1, double x2, double epsilon) {
    return abs(x1 - x2) < epsilon;
}

double solveEquation(double initialGuess, double epsilon, int maxIterations) {
    double x0 = initialGuess;
    double x1 = nextIteration(x0);
    int iterations = 1;

    while (!isConverged(x0, x1, epsilon) && iterations < maxIterations) {
        x0 = x1;
        x1 = nextIteration(x0);
        iterations++;
    }

    return x1;
}

int main() {
    double initialGuess = 1.0;
    double epsilon = 1e-6;
    int maxIterations = 1000;

    double solution = solveEquation(initialGuess, epsilon, maxIterations);

    cout << "Solution: " << solution << endl;

    return 0;
}
