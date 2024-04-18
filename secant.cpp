#include <iostream>
#include <cmath>

using namespace std;

double equationFunction(double x) {
    return tan(x) - x;
}

double secantMethod(double x0, double x1, double epsilon, int maxIterations) {
    double x = x1;
    double xPrev = x0;
    int iterations = 0;

    while (fabs(equationFunction(x)) > epsilon && iterations < maxIterations) {
        double temp = x;
        x = x - equationFunction(x) * (x - xPrev) / (equationFunction(x) - equationFunction(xPrev));
        xPrev = temp;
        iterations++;
    }

    return x;
}

int main() {
    double initialGuess1 = 1.0; 
    double initialGuess0 = 0.5;
    double epsilon = 1e-6; 
    int maxIterations = 1000; 

    double solution = secantMethod(initialGuess0, initialGuess1, epsilon, maxIterations);

    cout << "Solution: " << solution << endl;

    return 0;
}
