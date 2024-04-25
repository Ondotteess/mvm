#include <iostream>
#include <complex>
#include <limits>

using namespace std;

complex<double> func(complex<double> z) {
    return pow(z, 3.0) - 1.0;
}

complex<double> der(complex<double> z) {
    return 3.0 * pow(z, 2.0);
}

complex<double> newton(complex<double> init, double eps, int iters) {
    complex<double> z = init;
    int curr_iters = 0;

    while (abs(func(z)) > eps && curr_iters < iters) {
        z = z - func(z) / der(z);
        curr_iters++;
    }

    return z;
}

int determineRoot(const complex<double>& z, double eps, int iters) {
    complex<double> root1 = 1.0;
    complex<double> root2 = -0.5 + 0.5i * sqrt(3);
    complex<double> root3 = -0.5 - 0.5i * sqrt(3);

    complex<double> newton_result = newton(z, eps, iters);

    if (abs(newton_result - root1) < eps)
        return 1;
    else if (abs(newton_result - root2) < eps)
        return 2;
    else if (abs(newton_result - root3) < eps)
        return 3;
    else
        return 0; 
}


int main() {
    double eps = 1e-6;
    int iters = 1000;
    const int area = 50;

    double x_min = -2.0;
    double x_max = 2.0;
    double y_min = -2.0;
    double y_max = 2.0;
    double step = 0.1;

    int root_region[area][area];

    for (int i = 0; i < area; i++) {
        double x = x_min + i * step;
        for (int j = 0; j < area; j++) {
            double y = y_min + j * step;
            complex<double> init_point(x, y);
            root_region[i][j] = determineRoot(init_point, eps, iters);
        }
    }

    cout << "Approximate regions of attraction for roots of z^3 - 1:\n";
    for (int i = 0; i < area; i++) {
        for (int j = 0; j < area; j++) {
            cout << root_region[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}
