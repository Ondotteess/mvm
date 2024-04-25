#include <iostream>
#include <complex>

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

int main() {
    double eps = 1e-6;
    int iters = 1000;

    complex<double> init[3] = { complex<double>(2.3, 0.0),
                                complex<double>(-0.424, 0.2235 * sqrt(3.0)),
                                complex<double>(-0.3523, -0.152 * sqrt(3.0)) };

    cout << "Solutions z^3 - 1:\n";
    for (int i = 0; i < 3; ++i) {
        complex<double> root = newton(init[i], eps, iters);
        cout << "Solution: " << i + 1 << ": " << root.real() << " + i*" << root.imag() << endl;
    }
    /* 
        ROOTS:
            1 + 0i
            -1/2 - i*sqrt(3)/2 
            -1/2 + i*sqrt(3)/2
    */
    return 0;
}
